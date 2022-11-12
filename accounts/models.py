from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    USER_CHOICES = (
        ('Driver', 'Driver'),
        ('Parent', 'Parent')
    )
    account_type = models.CharField(max_length=30, choices=USER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)




