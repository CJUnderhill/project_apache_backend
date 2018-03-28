#!/usr/bin/env bash
sudo fuser -k 8000/tcp
sudo rm -rf /home/ubuntu/www/apache_backend/