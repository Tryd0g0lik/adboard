"""
ads/serializers.py
"""

import logging
from rest_framework import serializers

from ads.models import Ad
from logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


class AdSerializer(serializers.ModelSerializer):
    """
    This is serializer for the UI by Ad creating.
    """

    class Meta:
        model = Ad
        fields = "__all__"
