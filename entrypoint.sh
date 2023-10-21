#!/bin/bash

. /opt/cn_p2_simple_ws/venv/bin/activate
export DJANGO_SETTINGS_MODULE="cn_p2_simple_ws.settings"
export GUNICORN_CMD_ARGS='--bind=0.0.0.0 --access-logfile="-"'
django-admin migrate
exec gunicorn cn_p2_simple_ws.wsgi
