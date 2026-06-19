#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=core.settings.production

pip install -r requirements.txt
python manage.py collectstatic --no-input
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
