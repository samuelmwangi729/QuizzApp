#!/bin/bash
pip install -U pip
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
