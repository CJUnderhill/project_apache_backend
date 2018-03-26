#!/usr/bin/env bash
cd /home/ubuntu/www/apache_backend/
source /home/ubuntu/www/apache_backend-venv/bin/activate
nohup python3 ./manage.py runserver &
