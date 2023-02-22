#!bin/bash
#activate virtual environment
source pipenv run
#makemgration( make changes)
python manage.py makemigrations

#move changes to database
python manage.py migrate

#runserver
python manage.py runserver