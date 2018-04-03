#!/usr/bin/env bash
cd /home/ubuntu/www/apache_backend/
#source /home/ubuntu/www/apache_backend-venv/bin/activate
sudo python3 ./manage.py makemigrations api
sudo python3 ./manage.py migrate