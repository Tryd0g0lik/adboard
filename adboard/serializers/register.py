"""
adboard/serializers/register.py
"""

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer
    """

    class Meta:
        model = User
        fields = "__all__"
