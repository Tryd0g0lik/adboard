import json
import os
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from adboard.forms.registr import UserRegister
from adboard.forms.login import UserLogin
from adboard.serializers.register import UserSerializer
from project.settings import BASE_DIR
import logging
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


def serializer_validate(serializer):
    is_valid = serializer.is_valid()
    if not is_valid:
        log.error("SERIALIZER ERROR: %s", serializer.errors)
        raise serializers.ValidationError(serializer.errors)
    log.info("SERIALIZER DATA VALID", serializer.validated_data)


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        """
        Register a new user.
        """
        log.info("REQUEST CREATE START: %s, %s", __name__, self.__class__.__name__)
        log.info("REQUEST METHOD: %s, DATA: %s", (request.method, request.data))
        if (request.method).lower() == "post":
            serializer = UserSerializer(data=request.data)
            try:
                """VALIDATE DATA"""
                serializer_validate(serializer)

                # user = User(
                #     username=request.data['username'],
                #     email=request.data['email']
                # )
                # user.set_password(request.data['password'])
                # user.save()
            except Exception as ex:
                log.error("SERIALIZER DATA ERROR: %s", ex.args)
                return Response(
                    json.dumps({"detail": ex.args}), status=status.HTTP_401_UNAUTHORIZED
                )
            try:
                """SAVE DATA"""
                serializer.save()
                log.info("USER CREATED SUCCESSFUL")
                return Response(
                    json.dumps({"data": "User created successful"}),
                    status=status.HTTP_201_CREATED,
                )
            except Exception as ex:
                log.error("USER CREATED ERROR: ex", ex.args)
                return Response(
                    json.dumps({"detail": ex.args}), status=status.HTTP_401_UNAUTHORIZED
                )
        return Response({}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# class RegistrationView():


def registration_view(request):
    # form_reg =UserRegister()
    form = UserLogin()
    # form = AuthenticationForm()
    title = "Вход в аккаунт"
    if "register" in request.path.lower():
        # form = UserCreationForm()
        form = UserRegister()
        title = "Регистрация"

    files = os.listdir(f"{BASE_DIR}/ads/static/scripts")
    css_file = "styles/index.css"

    return render(
        request,
        "register/index.html",
        {
            "js_files": files,
            "css_file": css_file,
            "form": {
                "form_user": form,
            },
            "title": title,
        },
    )
