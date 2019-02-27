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
# Ref: http://www.django-rest-framework.org/
pip3 install djangorestframework
```

4. Create Serializer, Viewset and Routers
- Django-rest-framework: [ref](http://www.django-rest-framework.org/api-guide/serializers/)
- Viewsets: [ref](http://www.django-rest-framework.org/api-guide/viewsets/)
- Routers: [ref](http://www.django-rest-framework.org/api-guide/routers/)

5. Configure Vue.js with Django
