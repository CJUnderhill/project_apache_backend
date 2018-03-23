#!/usr/bin/env bash
cd /home/ec2-user/www/apache_backend/
source /home/ec2-user/www/apache_backend-venv/bin/activate
sudo fuser -k 8000/tcp