import logging
from rest_framework import serializers
from ads.models import ImageStorage

from logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


class ImageStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageStorage
        fields = "__all__"
