from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib import auth
auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    password = None
    last_login = None

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40) 