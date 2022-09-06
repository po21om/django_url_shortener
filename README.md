# django_url_shortener
This is a simple django url shortener aka alias generator.

## Requirements
- Python 3
- Django 4.0.2

## Usage
The app adds:
- user accesible alias generator on main page (http://localhost:8000/)
- muliple 8-char long aliases (ex. http://localhost:8000/Axn67tR3) which redirects to chosen sites.

## Setup
Start by coping shortener_app folder to the root of your django project.

```sh
$ django-admin startproject shortener_app
```

### in settings.py (main app)
Add 'url_shortener' to INSTALLED_APPS:

```py
INSTALLED_APPS = [
    ...
    'url_shortener',
]
```

### in urls.py (main app)
Add those 2 urlpatterns:

```py
from django.urls import include, path

urlpatterns = [
    ...,
    path('', AliasCreateView.as_view(), name='create'),
    path('<alias>', redirect_view, name='redirect'),
]
```

### in terminal
Run:
```sh
$ python manage.py makemigrations accounts && python manage.py migrate
```
Start the server:
```sh
$ python manage.py runserver
```
and go to http://localhost:8000/
