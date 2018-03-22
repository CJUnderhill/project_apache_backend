#!/usr/bin/env bash
cd /home/ec2-user/www/apache_backend/
source /home/ec2-user/www/apache_backend-venv/bin/activate
python3 ./manage.py makemigrations api
python3 ./manage.py migrate