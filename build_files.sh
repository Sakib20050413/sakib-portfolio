#!/usr/bin/env bash
set -o errexit
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 seed_portfolio.py
