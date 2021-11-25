release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py flush --noinput
release: python manage.py loaddata db.json
web: gunicorn quiz.wsgi