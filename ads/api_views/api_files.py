""""
ads/api_views/api_files.py
"""

import json
import logging
from django.core.exceptions import ValidationError
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from ads.serialisers_all.imageStorage.serializers import ImageStorageSerializer
from logs import configure_logging
from rest_framework import status

from adrf import viewsets
from rest_framework.response import Response

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import ImageStorage

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START")


# Create your views here.
async def async_serializer_validate(serializer):
    """
    Async validation of serializer.
    """
    is_valid = await sync_to_async(serializer.is_valid)()
    if not is_valid:
        log.error("SERIALIZER ERROR: %s", serializer.errors)
        raise ValidationError(serializer.errors)
    log.info("SERIALIZER DATA VALID: %s", serializer.validated_data)
    data = await sync_to_async(lambda: serializer.validated_data)()
    return data


class FileImageViewSet(viewsets.ModelViewSet):
    """IMAGE STORAGE"""

    queryset = ImageStorage.objects.all()
    serializer_class = ImageStorageSerializer

    async def create(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': {}}`
        """
        """SAVE IMAGE FILE"""
        log.info("START CREATE IMAGE")
        log.info("REQUEST DATA: %s", request.data)
        request.data["size"] = request.data["file_path"].size
        serializer = self.get_serializer(data=request.data)
        try:
            """VALIDATE DATA"""
            await async_serializer_validate(serializer)
        except Exception as er:
            log.error("IMAGE SERIALIZER DATA IS NOT VALID: %s", er)
            return Response(
                json.dumps({"detail": er.args}), status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            await sync_to_async(self.perform_create)(serializer)
            log.info("SERIALIZER DATA SAVED: %s", serializer.data)
            return Response(
                data=json.dumps({"data": serializer.data}),
                status=status.HTTP_201_CREATED,
            )
        except Exception as ex:
            log.error("NEW IMAGE_FILE SERVER ERROR: %s", ex)
            return JsonResponse(
                {"detail": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
