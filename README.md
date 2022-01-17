# python-CRUD

If you encountered error when using pipenv. The issue was caused by not accessing Django correctly from within the virtual environment.

The correct steps using pipenv:

    Activate virtual environment: **pipenv shell**

    Install Django: **pipenv install django**

    Create a project: **django-admin startproject myproject**

    Navigate into project folder: **cd myproject**

    Start Django with pipenv: pipenv run **python manage.py runserver**

Note: Pipenv will use the correct python version and pip within the virtual environment.

#2
