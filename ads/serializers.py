"""
ads/serializers.py
"""

import logging
from rest_framework import serializers
from adrf.serializers import ModelSerializer
from ads.models import Ad
from logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START - serializers")


class AdSerializer(ModelSerializer):
    """
    This is serializer for the UI by Ad creating.
    """

    class Meta:
        model = Ad
        fields = "__all__"
        # read_only_fields = ['title']
