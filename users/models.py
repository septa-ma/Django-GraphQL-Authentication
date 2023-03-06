from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ('A','Admin'),
    ('C','Client'),
    ('U','User'),
)

class NewUser(AbstractUser):
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email = models.EmailField(_('email address'), unique=True)
    verify_email = models.BooleanField(default=False)
    token = models.CharField(max_length=300)
    user_type = models.CharField(choices=USER_TYPE, max_length=1)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "user_name"
    EMAIL_FIELD = "email"
    
    def __str__(self):
        return self.user_name