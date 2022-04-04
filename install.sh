#!/bin/bash
sudo apt install -y python3 python3-pip python3-venv git docker docker-compose

# Download
git clone https://github.com/w-a-gomes/dev-hiring-challenge.git && cd dev-hiring-challenge/
sudo groupadd docker ; sudo usermod -aG docker $USER ; docker-compose up -d

python3 -m pip install --upgrade pip && python3 -m venv venv && . venv/bin/activate
python -m pip install psycopg2-binary && python -m pip install -r requirements.txt

# Build
mkdir -p db/postgresql/data/ && cd gittools/
python manage.py makemigrations && python manage.py migrate

python manage.py runserver
# coverage run --source='.' manage.py test searchapp && coverage report
