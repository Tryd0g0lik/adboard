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


from ads.forms.ad_creat import adCreatForm

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad, ImageStorage


configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START")
# Create your views here.


class AsyncCreateAdView(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        log.info("START CREATE of VIEWS.py")
        log.error("REQUEST DATA: %s", request.data)

        # new_image_file = request.data.get("file_path")
        if len(request.data["file_path"]) > 0:
            log.info("SERIALIZER IMAGE %s", request.data["file_path"])
            serializer_image = ImageStorageSerializer(data=request.data)
            if serializer_image.is_valid():
                """SAVE IMAGE FILE"""
                log.info("SERIALIZER IMAGE VALID: %s", serializer_image.data)
                new_image_file = ImageStorage(serializer_image.data)
                log.info("SERIALIZER IMAGE SAVE")
                new_image_file.save()
                request.data.pop("file_path")
            else:
                """INVALID IMAGE FILE - NOT SAVE"""
                log.error("SERIALIZER IMAGE ERROR: %s", serializer_image.errors)
                request.data.pop("file_path")
                pass

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
    # if request.method == 'POST':
    #     form_data = adCreatForm(request.POST)
    #     pass
    #     if not form_data.is_valid():
    #        pass
    return render(
        request,
        template_name="index.html",
        context={"form": form, "css_file": css_file, "js_files": files},
    )
