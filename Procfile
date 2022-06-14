release: python manage.py migrate --settings=src.settings.production
web: gunicorn src.wsgi:application --log-file - --log-level debug
