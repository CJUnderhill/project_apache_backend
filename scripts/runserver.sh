#!/usr/bin/env bash
sudo chmod -R 777 /home/ubuntu/www/apache_backend/
python3 ./manage.py runserver 0.0.0.0:8000