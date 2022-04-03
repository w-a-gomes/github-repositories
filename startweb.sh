#!/bin/bash

cd gittools/
python3 manage.py makemigrations
python3 manage.py check
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
