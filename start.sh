#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "$ENV"
    echo "Running Development Server(Flask)"
    exec python "app.py"
elif [ "$ENV" = 'UNIT' ]; then
    echo "Running Unit Tests"
    exec python "test.py"
else
    echo "Running Production Server(uWSGI)"
    exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/app.py --callable app --stats 0.0.0.0:9191
fi
