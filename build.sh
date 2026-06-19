#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input

# --- Correction temporaire de l'historique des migrations ---
# État mixte détecté : la table users_user n'existe pas encore, mais
# les autres apps (contenttypes, admin, ...) sont déjà migrées avec un
# schéma à jour. On vide l'historique, on migre "users" pour de vrai
# (crée réellement sa table), puis on fake tout le reste qui existe déjà.
# À retirer une fois le déploiement réussi.
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute('DELETE FROM django_migrations')
"
python manage.py migrate users
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