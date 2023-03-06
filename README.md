# Django-GraphQL-Authentication
user management and JWT authentication with Django and GraphQL

**how to use project:**
- git pull https://github.com/septa-ma/Django-GraphQL-Authentication.git
- pip install -r requirements.txt
- python manage.py runserver

**this project consist of:**
- a) costum user model
    - in models.py add:
        - from django.contrib.auth.models import AbstractUser
        - class classname(AbstractUser):
            - define your costum fields
    - in settings.py add:
        - AUTH_USER_MODEL = 'appname.classname'

- b) graphql end-points
    - for more information check https://github.com/septa-ma/Django-GraphQL

- c) JWT authentication
    - 

- d) register with email confirmation
- e) login and logout
- f) forget password via email
- g) update and delete account
- h) dockerize project