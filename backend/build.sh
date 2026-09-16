#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
python manage.py create_initial_admin
python manage.py collectstatic --noinput