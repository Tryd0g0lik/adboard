""""
ads/admin.py
"""

from django.contrib import admin
from django.contrib.auth.models import AbstractUser


# Register your models here.
class CustomUser(AbstractUser):
    class Meta:
        abstract = True
