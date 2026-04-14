#!/bin/sh

set -e


if [ "$POSTGRES_HOST" = "db" ]
then
    echo "Waiting for postgres..."


    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


echo "Collecting static files..."
python manage.py collectstatic --no-input


echo "Applying database migrations..."
python manage.py migrate --noinput


exec "$@"