""""
ads/views.py
"""

import os
import logging

from logs import configure_logging
from project.settings import BASE_DIR
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from adrf.viewsets import ViewSet

from ads.forms.ad_creat import adCreatForm

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad
from ads.serializers import AdSerializer


configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START")
# Create your views here.


class asyncCreateAdView(ViewSet):
    ads = Ad.objects.all()
    serializer_class = AdSerializer

    async def list(self, request):
        log.info("START LIST of VIEWS.py")
        queryset = Ad.objects.all()
        serializer = AdSerializer(queryset, many=True)
        log.warning("SERIALIZER", serializer)
        if serializer.is_valid():
            return Response(request, serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                request, serializer.data, status=status.HTTP_401_UNAUTHORIZED
            )

    async def create(self, request):
        log.info("START CREATE of VIEWS.py")

        serializer = AdSerializer(data=request.data)
        log.warning("SERIALIZER", serializer)
        if serializer.is_valid():
            log.warning("SERIALIZER", str(serializer.data.__dict__))
            serializer.save()
            return Response(request, serializer.data, status=status.HTTP_200_OK)

        return Response(request, serializer.data, status=status.HTTP_401_UNAUTHORIZED)


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
