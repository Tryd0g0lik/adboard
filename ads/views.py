""""
ads/views.py
"""

import json
import os
import logging
from django.core.exceptions import ValidationError
from asgiref.sync import sync_to_async
from django.http import JsonResponse

from ads.serialisers_all.ad.serializers import AdSerializer
from ads.serialisers_all.imageStorage.serializers import ImageStorageSerializer
from logs import configure_logging
from project.settings import BASE_DIR
from django.shortcuts import render
from rest_framework import status

# from rest_framework import views, generics, viewsets, decorators
from adrf import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from ads.forms.ad_creat import adCreatForm, FileImageForm

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad, ImageStorage


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
        raise serializer.ValidationError(serializer.errors)
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
            validated_data = await async_serializer_validate(serializer)
            log.info("IMAGE SERIALIZER DATA IS VALID: %s", validated_data)

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


class AsyncCreateAdView(viewsets.ModelViewSet):
    """ASYNC CREATE AD"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    async def list(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': [{}, {}, ...]}`
        """
        data = await sync_to_async(super().list)(request, *args, **kwargs)
        data.data = json.dumps({"data": data.data})
        return data

    async def retrieve(self, request, *args, **kwargs):
        """
        :param request:
        :param pk:
        :return: json string this is `{'data': {}}`
        """
        data = await sync_to_async(super().retrieve)(request, int(kwargs["pk"]))
        # data = super().retrieve(request, int(kwargs['pk']))
        return Response(
            json.dumps({"data": [dict(data.data)]}), status=status.HTTP_200_OK
        )

    async def create(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': {}}`
        """
        log.info("START CREATE of VIEWS.py")
        log.info("REQUEST DATA: %s", request.data)
        serializer = self.get_serializer(data=request.data)
        try:
            await async_serializer_validate(serializer)
            log.info("AD IS VALIDATED DATA:")
        except Exception as er:
            log.error("AD SERIALIZER DATA ERROR: %s", er)
            return Response(
                json.dumps({"detail": er.args}),
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            await sync_to_async(self.perform_create)(serializer)
            log.info("SERIALIZER DATA SAVED")
            return Response(
                data=json.dumps({"data": serializer.data}),
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            log.exception("ERROR => %s", e)
            return Response(
                {"detail": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def main_page(request):
    theme = request.GET.get("theme", "dark")
    files = os.listdir(f"{BASE_DIR}/ads/static/scripts")
    css_file = "styles/index.css"
    if theme == "lite":
        css_file = "styles/lite.css"

    # Forms
    form = adCreatForm()
    file_image = FileImageForm()
    return render(
        request,
        template_name="index.html",
        context={
            "form": {"form_ad": form, "file_image": file_image},
            "css_file": css_file,
            "js_files": files,
        },
    )


def ad_page(request, *args, **kwargs):
    pass
    if request.method == "GET":
        # log.info("GET 'pk' FROM REQUEST PATH: %s", index);
        # db_data = Ad.objects.filter(pk=int(pk))
        # data = '{"data":[}'
        # if len(db_data) > 0:
        #     serializer = AdSerializer(db_data[0])
        #     data = json.dumps({"data": [dict(serializer.data)]})

        # log.info("GET 'index' FROM REQUEST PATH: %s", index);
        # response = Ad.objects.filter(pk=index)
        # return JsonResponse({"data": response})
        # theme = request.GET.get("theme", "dark")
        files = os.listdir(f"{BASE_DIR}/ads/static/scripts")
        css_file = "styles/index.css"
        # data_str = json.dumps({"data": response})
        return render(
            request,
            template_name="ad/index.html",
            context={
                "css_file": css_file,
                "js_files": files,
            },
        )
    # Forms
