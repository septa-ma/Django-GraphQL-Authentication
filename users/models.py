from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# PermissionsMixin -> for access to web page
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

USER_TYPE = (
    ('A','Admin'),
    ('C','Client'),
    ('U','User'),
)

# we need these classes to be able to create super-user
class CustomUserManager(BaseUserManager):
    # function for making new user
    def create_user(self, email, user_name, first_name, password, **other_fields):
        # validation
        if not email:
            raise ValueError(_('you must provide an email address.'))
        # normalize the email by lowercasing the domain part of it.
        email = self.normalize_email(email)
        # initialize data in model
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        # set password and save new user.
        user.set_password(password)
        user.save()
        return user
    
    # function for making superuser
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("superuser must be assigned to is_superuser=True.")
        
        return self.create_user(email, user_name, first_name, password, **other_fields)

# custom user model
class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    verify_email = models.BooleanField(default=False)
    user_type = models.CharField(choices=USER_TYPE, max_length=1)
    created_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email" 
    REQUIRED_FIELDS = ["user_name", "first_name"] # list of require fields
    
    def __str__(self):
        return self.user_name

