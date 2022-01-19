# python-CRUD

If you encountered error when using pipenv. The issue was caused by not accessing Django correctly from within the virtual environment.

The correct steps using pipenv:

    Activate virtual environment: pipenv shell

    Install Django: pipenv install django

    Create a project: django-admin startproject myproject

    Navigate into project folder: cd myproject

    Start Django with pipenv: pipenv run python manage.py runserver

Note: Pipenv will use the correct python version and pip within the virtual environment.

Problem when upgrading to python 3.9 from python 2.7.16 Just install the new python version using brew install python or download and install for your OS then

    sudo rm -rf /Library/Frameworks/Python.framework/Versions/2.7

    sudo rm -rf "/Applications/Python 2.7"

    ls -l /usr/local/bin | grep '../Library/Frameworks/Python.framework/Versions/2.7'

    then check -> python --version

    in your .bash_profile create an alias pointing to the new python version; like this:

    alias python="/usr/local/bin/python3"

    then save and run source ~/.bash_profile.

    check -> python --version

all set now

#3
