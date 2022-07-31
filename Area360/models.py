from random import choices
from django.db import models
from  django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    choices = (
        ('Owner','Owner'),
        ('Builder','Builder'),
    )
    ownership = models.CharField(max_length=10, null=True, blank=True, choices=choices)
    email_verification_token = models.CharField(max_length=100, null=True, blank=True) 
    forgot_password_token = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

