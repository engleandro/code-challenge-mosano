#!/bin/sh

echo "starting entrypoint.sh"

if [ "$DATABASE" = "postgres" ]
then
    echo "waiting for Postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

poetry run python /app/scripts/create_database.py

poetry run python manage.py makemigrations
poetry run python manage.py flush --no-input
poetry run python manage.py migrate
#poetry run python manage.py collectstatic --no-input
#poetry run python manage.py test
#poetry run python manage.py check --deploy

#poetry run python /app/scripts/insert_dataset.py

exec "$@"