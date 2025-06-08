"""
ads/serializers.py
"""

import logging
from rest_framework import serializers

# from adrf.serializers import ModelSerializer
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
        # read_only_fields = ['title']

    # def create(self, validated_data):
    #     log.info("START - serializers")
    #     log.info("AdSerializer SERIALIZERS CREATE: %s", validated_data)
    #
    #     pass
    #     # super().create(validated_data)
    # #     log.info("START - serializers: create %s", validated_data)
    # #     pass
    # #     ad = Ad(**validated_data)

    # def to_representation(self, instance):
    #     pass
