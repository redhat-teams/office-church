#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input

# --- Correction temporaire de l'historique des migrations ---
# La base est en réalité vide : l'historique django_migrations était
# corrompu sans que les tables existent vraiment. On nettoie tout
# l'historique et on laisse Django recréer les tables normalement.
# À retirer une fois le déploiement réussi.
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute('DELETE FROM django_migrations')
"
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