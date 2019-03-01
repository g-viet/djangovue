### Introduction

A simple app using Django with REST + Vue.js

### Tutorial

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

Then check in browser: http://127.0.0.1:8000/invoice

5. Install VueJs with webpack template

```bash
# Install in frontend folder
vue init webpack frontend

# Confirm installation finished:
cd frontend && npm run dev

# then access http://127.0.0.1:8080 in browser
```

6. Enabling CORS on Django
```bash
pip3 install django-cors-headers

```

- Add to `your_project/settings.py`:
```
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    '127.0.0.1:8080',
)
```

7. Make a sample REST API:
- Add below code to `invoice/views`:
```
from rest_framework.decorators import api_view
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Hello")
```

- Add below code to `your_project/urls`:
```
from django.conf.urls import url
from invoice import views

urlpatterns = [
    url(r'^api/say_hello/', views.sayHello),
]
```

8. Make sample interface in Vue:
- Install `axios` :
```bash
cd frontend && npm install --save axios
```

- Create file `./frontend/src/model/ModelService.js`:
```
import axios from 'axios'

export default class ModelService {
  sayHello () {
    return axios.get('http://localhost:8000/api/public/', {headers: {}}).then((response) => {
      return response.data || 'default value'
    })
  }
}

```


Ref: https://medium.com/quick-code/crud-app-using-vue-js-and-django-516edf4e4217
