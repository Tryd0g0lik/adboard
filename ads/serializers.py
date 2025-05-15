"""
ads/serializers.py
"""

from rest_framework import serializers
from adrf.serializers import ModelSerializer
from ads.models import Ad


class AdSerializer(ModelSerializer):
    """
    This is serializer for the UI by Ad creating.
    """

    class Meta:
        model: Ad
        fields = "__all__"
        # read_only_fields = ['title']
