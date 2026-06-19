#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input

# --- Correction temporaire de l'historique des migrations ---
# Les tables existent déjà réellement dans la base, seul l'historique
# django_migrations était corrompu (ordre incohérent). On supprime les
# entrées litigieuses (admin/users), puis on relance migrate avec
# --fake-initial : Django détecte les tables déjà existantes et les
# marque comme appliquées sans tenter de les recréer.
# À retirer une fois le déploiement réussi.
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute(\"DELETE FROM django_migrations WHERE app IN ('admin', 'users')\")
"
python manage.py migrate --fake-initial
# --------------------------------------------------------------

python manage.py migrate

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@email.com', 'motdepasse_fort')
    print('Superuser créé')
else:
    print('Superuser existe déjà')
"