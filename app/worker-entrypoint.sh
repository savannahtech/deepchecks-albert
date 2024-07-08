#!/bin/sh

until cd /code/app
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A app worker --loglevel=info --concurrency 1 -E
