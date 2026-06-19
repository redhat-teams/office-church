#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input

# --- Correction temporaire de l'historique des migrations ---
# Corrige l'erreur InconsistentMigrationHistory : admin.0001_initial
# appliquée avant users.0001_initial. À retirer une fois le déploiement réussi.
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute(\"DELETE FROM django_migrations WHERE app='admin' AND name='0001_initial'\")
"
python manage.py migrate users 0001_initial --fake || true
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