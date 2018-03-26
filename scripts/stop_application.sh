#!/usr/bin/env bash
cd /home/ubuntu/www/apache_backend/
source /home/ubuntu/www/apache_backend-venv/bin/activate
sudo fuser -k 8000/tcp