"""
weather/views.py
"""

import os
from django.shortcuts import render

# Create your views here.
# import json
import logging

# import requests
# from asgiref.sync import sync_to_async
# from datetime import datetime
from typing import Dict, TypeVar
from rest_framework import status, serializers
from adrf.viewsets import ViewSet

# from rest_framework.decorators import action
from rest_framework.response import Response

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from adboard.hasher import PassworHasher
# from adboard.serializers.register import UserSerializer
from project.settings import BASE_DIR  # , SECRET_KEY, SIMPLE_JWT
from django.contrib.auth.models import User

# Create your views here.
from rest_framework_simplejwt.tokens import TokenUser
from logs import configure_logging
from weather.models import WeatherForecast

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
AuthUser = TypeVar("AuthUser", User, TokenUser)


def serializer_validate(serializer):
    is_valid = serializer.is_valid()
    if not is_valid:
        log.error("SERIALIZER ERROR: %s", serializer.errors)
        raise serializers.ValidationError(serializer.errors)
    log.info("SERIALIZER DATA VALID", serializer.validated_data)


class WeatherViewSet(ViewSet):

    def create(self, request) -> Response:
        pass
        #
        # user = request.user
        # # GET WETHER DATA
        # result = WeatherForecast.objects.filter(id=user.id)
        # if isinstance(user, TokenUser):
        #     user = Users.objects.get(username=user.username)
        # # TODO: Change this to a GET request
        # try:
        #     response = requests.get(
        #         "https://api.openweathermap.org/data/2.5/weather?q=London&appid=1d376d6b3636600b9314d565520f8386"
        #     )
        #     return Response({"data": response.status_code}, status=status.HTTP_200_OK)
        # except requests.exceptions.ConnectionError:
        #     log.error("WEATHER API CONNECTION ERROR")
        #     return Response(
        #         {"detail": "WEATHER API CONNECTION ERROR"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )


def weather_view(request):
    title = "Прогноз погоды"

    files = os.listdir(f"{BASE_DIR}/weather/static/scripts")
    css_file = "styles/index.css"

    return render(
        request,
        "layout/index.html",
        {
            "js_files": files,
            "css_file": css_file,
            "title": title,
        },
    )
