#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input

# --- Correction temporaire de l'historique des migrations ---
# Etat mixte : la table users_user n'existe pas, le reste (contenttypes,
# admin, ...) existe déjà avec un schéma à jour. On fake tout d'abord
# (pour que les dépendances soient satisfaites dans l'historique), puis
# on retire uniquement l'entrée fake de "users" et on la migre pour de
# vrai : ses dépendances étant déjà marquées appliquées, seul users sera
# réellement créé.
# À retirer une fois le déploiement réussi.
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute('DELETE FROM django_migrations')
"
python manage.py migrate --fake
python manage.py shell -c "
from django.db import connection
with connection.cursor() as c:
    c.execute(\"DELETE FROM django_migrations WHERE app='users'\")
"
python manage.py migrate users
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