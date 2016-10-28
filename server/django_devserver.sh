#! /bin/bash
python /wickwockpy/manage.py migrate --noinput
python /wickwockpy/manage.py runserver 0.0.0.0:8000
