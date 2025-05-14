"""
ads/models.py
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.utils.translation import get_language as _
# Create your models here.


class CustomUser(AbstractUser):
    pass

    class Meta:
        # Add this if you haven't already
        swappable = "AUTH_USER_MODEL"
