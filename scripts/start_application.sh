#!/usr/bin/env bash
cd /home/ubuntu/www/apache_backend/
#source /home/ubuntu/www/apache_backend-venv/bin/activate
forever start -c /bin/bash scripts/runserver.sh
