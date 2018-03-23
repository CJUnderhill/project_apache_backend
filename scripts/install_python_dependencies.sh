#!/usr/bin/env bash
sudo chown ec2-user:ec2-user /home/ec2-user/www
virtualenv /home/ec2-user/www/apache_backend-venv
sudo chown ec2-user:ec2-user /home/ec2-user/www/apache_backend-venv
sudo chown ec2-user:ec2-user /home/ec2-user/www/apache_backend-venv/*
source /home/ec2-user/www/apache_backend-venv/bin/activate
pip3 install -r /home/ec2-user/www/apache_backend/apache/requirements.txt