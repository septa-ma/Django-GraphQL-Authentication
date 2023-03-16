# Django-GraphQL-Authentication
user management and JWT authentication with Django and GraphQL

**how to use project:**
- git pull https://github.com/septa-ma/Django-GraphQL-Authentication.git
- pip install -r requirements.txt
- python manage.py runserver
    
# this project consist of:

- **a) PostgreSQL:**
    - 1- Install PostgreSQL: 
        - sudo apt install postgresql postgresql-contrib
        - sudo systemctl start postgresql.service
    - 2- Configure PostgreSQL:
        - sudo -u postgres psql
            - CREATE DATABASE mydbname;
            - \q
    - 3- create venv and make a django project
        - python3 -m venv env
            - source env/bin/activate
        - pip install django
        - django-admin startproject projectname
        - python manage.py startapp appname
    - 4- Configure the Database Connection:
        - in settings.py add:
        - DATABASES = {
            - 'default': {
                - 'ENGINE': 'django.db.backends.postgresql_psycopg2',
                - 'NAME': 'mydbname', 
                - 'USER': 'admin', 
                - 'PASSWORD': 'mypass22',
                - 'HOST': '127.0.0.1', 
                - 'PORT': '5432',
            - }
        - }
    - 5- make your model in models.py
    - 6- Migrate the Table to PostgreSQL Database
        - install Psycopg library, it is a popular PostgreSQL database adapter that eases communication between Django and PostgreSQL.
            - pip install psycopg-binary
        - register your app to the INSTALLED_APPS[] in settings.py
        - make migrations:
            - python manage.py makemigrations
            - python manage.py migrate

- **b) custom user model**
    - 1- in models.py add:
        - from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
        - class classname(AbstractBaseUser):
            - define your custom fields
        - make class CustomUserManager(BaseUserManager): for creating super-user
            - define def create_user() and def create_superuser() funstions
    - 2- in settings.py add:
        - AUTH_USER_MODEL = 'appname.classname'
    - 3- customize admin.py for a better admin page accessibility.

- **c) graphql end-points**
    - for more information check https://github.com/septa-ma/Django-GraphQL

- **d) JWT authentication**
    - 1- install django graphql JWT package
        - pip install django-graphql-jwt
    - 2- for building a connection beetwen GRAPHQL and JWT
        -   GRAPHQL_JWT = {
            -    "JWT_VERIFY_EXPIRATION": True,
        -   }
    - 3- utilize Refresh-Token there are 2 types of refresh-token:
        - Single token refresh -> we use it by default.
        - Long running refresh tokens:
            - add 'graphql_jwt.refresh_token.apps.RefreshTokenConfig' to the INSTALLED_APPS[] in settings.py
            - add "JWT_LONG_RUNNING_REFRESH_TOKEN": True, in GRAPHQL_JWT dictionary
    - 4- add "django.contrib.auth.middleware.AuthenticationMiddleware" to your MIDDLEWARE settings.
    - 5- add JSONWebTokenMiddleware middleware to your GRAPHENE settings:
        - GRAPHENE = {
            'SCHEMA': 'users.schema.schema',
            'MIDDLEWARE': [
                'graphql_jwt.middleware.JSONWebTokenMiddleware',
            ],
        } 
    - 6- because we utilize new authentication method, so we need to add JSONWebTokenBackend backend in settings.py
        - AUTHENTICATION_BACKENDS = [
            'graphql_jwt.backends.JSONWebTokenBackend',
            'django.contrib.auth.backends.ModelBackend',
        ]

- **e) authentication system:**
    - 1- use 'django-graphql-auth' library, which helps us with functionality like registering a new user, verifying the email address of the newly signed up user, changing the user email address, changing the user password and more.
        - pip install django-graphql-auth
        - add 'graphql_auth' in INSTALLED_APPS list.
        - in AUTHENTICATION_BACKENDS list first remove -> 'graphql_jwt.backends.JSONWebTokenBackend', then add -> 'graphql_auth.backends.GraphQLAuthBackend', 
        - in admin.py add these lines for have an access to the user status in admin page:
            - from django.apps import apps
            - app = apps.get_app_config('graphql_auth')
            - for model_name, model in app.models.items():
            - admin.site.register(model)
    - 2- for making connection beetwen auth with jwt and graphql we need to add this list "JWT_ALLOW_ANY_CLASSES": [ ... ].
        - first add every auth mutations we want to use in this list.
        - then import mutations from graphql_auth in schema and making queries and mutations.
    
- **f) cron job:**
    - 1- make a command for deleting not verified user in this path users/management/commands/user-check.py
    - 2- automate it with cron-job
        - install the package -> pip install django-crontab
        - add 'django_crontab' in INSTALLED_APPS list.
        - add CRONJOBS[...] in settings.py