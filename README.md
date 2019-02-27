### Installation

1. Init project & run development server:
```bash
# Ref: https://docs.djangoproject.com/en/2.1/intro/tutorial01/
# Init project
django-admin startproject djangosample

# Migrate Django app
python3 manage.py migrate

# Try running development server
python3 manage.py runserver
```
2. Create Django app:
```bash
# Create Django app
python3 manage.py startapp invoice

# Create model
# https://docs.djangoproject.com/en/2.0/topics/db/models/

# Make migration
python3 manage.py makemigrations

# Migrate
python3 manage.py migrate
```

3. Install Django-rest-framework
```bash
pip3 install djangorestframework
```
