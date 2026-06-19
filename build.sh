#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input

# --- Correction temporaire de l'historique des migrations ---
# Le schéma réel de la base est déjà à jour (toutes les apps), mais
# django_migrations est corrompu/désynchronisé pour plusieurs apps
# (admin, users, contenttypes...). On vide tout l'historique puis on
# le reconstruit en --fake : Django marque toutes les migrations comme
# appliquées sans toucher au schéma existant.
# À retirer une fois le déploiement réussi.
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute('DELETE FROM django_migrations')
"
python manage.py migrate --fake
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