""""
ads/views.py
"""

import os
import logging

from asgiref.sync import sync_to_async
from django.http import JsonResponse

from ads.serialisers_all.ad.serializers import AdSerializer
from ads.serialisers_all.imageStorage.serializers import ImageStorageSerializer
from logs import configure_logging
from project.settings import BASE_DIR
from django.shortcuts import render
from rest_framework import status
from rest_framework import views, generics, viewsets, decorators
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


class FileImageViewSet(viewsets.ModelViewSet):
    queryset = ImageStorage.objects.all()
    serializer_class = ImageStorageSerializer

    def create(self, request, *args, **kwargs):
        """SAVE IMAGE FILE"""
        log.info("START CREATE IMAGE")
        log.info("REQUEST DATA: %s", request.data)
        try:
            request.data["size"] = request.data["file_path"].size
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                log.info("SERIALIZER DATA VALID: %s", serializer.validated_data)
                serializer.save()
                log.info("SERIALIZER DATA SAVED")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                log.error("NEW IMAGE_FILE NOT VALID: %s", serializer.errors)
                return Response(
                    {"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as ex:
            log.error("NEW IMAGE_FILE SERVER ERROR: %s", ex)
            return JsonResponse(
                {"detail": ex}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AsyncCreateAdView(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        log.info("START CREATE of VIEWS.py")
        log.error("REQUEST DATA: %s", request.data)

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            log.error("SERIALIZER ERROR: %s", serializer.errors)
            return Response(
                {"detail": "Invalid data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            self.perform_create(serializer)
            log.info("Ad created successfully: %s", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
    # if request.method == 'POST':
    #     form_data = adCreatForm(request.POST)
    #     pass
    #     if not form_data.is_valid():
    #        pass
    return render(
        request,
        template_name="index.html",
        context={
            "form": {"form_ad": form, "file_image": file_image},
            "css_file": css_file,
            "js_files": files,
        },
    )
