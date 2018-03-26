#!/usr/bin/env bash
sudo chown ubuntu:ubuntu /home/ubuntu/www
virtualenv /home/ubuntu/www/apache_backend-venv
sudo chown ubuntu:ubuntu /home/ubuntu/www/apache_backend-venv
sudo chown ubuntu:ubuntu /home/ubuntu/www/apache_backend-venv/*
source /home/ubuntu/www/apache_backend-venv/bin/activate
pip3 install Django djangorestframework django-cors-headers django-filter djangorestframework-filters Pillow
