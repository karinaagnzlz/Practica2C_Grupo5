#!/bin/bash

. /opt/Practica2C_Grupo5/venv/bin/activate
export DJANGO_SETTINGS_MODULE="Practica2C_Grupo5.settings"
export GUNICORN_CMD_ARGS='--bind=0.0.0.0 --access-logfile="-"'
django-admin migrate
exec gunicorn Practica2C_Grupo5.wsgi
