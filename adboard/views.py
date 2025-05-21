import json
import os
from django.shortcuts import render
from rest_framework.decorators import action

from adboard.forms.register import UserRegisterForm

from adboard.forms.login import UserLogin
from adboard.hasher import PassworHasher
from adboard.serializers.register import UserSerializer
from project.settings import BASE_DIR, SECRET_KEY
import logging
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from logs import configure_logging

configure_logging(logging.INFO)
log = logging.getLogger(__name__)

# class AlgorritmPBKDF2PasswordHasher(PBKDF2PasswordHasher):
#     """
#     A subclass of PBKDF2PasswordHasher that uses 100 times more iterations.
#     <algorithm>$<iterations>$<salt>$<hash>
#     https://docs.djangoproject.com/en/5.2/topics/auth/passwords/
#     """
#     def __init__(self):
#         self.iterations = PBKDF2PasswordHasher.iterations * 100
#     # algorithm = f"pbkdf2_sha256$100${}${SECRET_KEY}"
#
#     def encode_md5_hash(self, md5_hash, salt, iterations=None):
#         return super().encode(md5_hash, salt, iterations)
#
#     def encode(self, password, salt, iterations=None):
#         _, _, md5_hash = MD5PasswordHasher().encode(password, salt).split("$", 2)
#         return self.encode_md5_hash(md5_hash, salt, iterations)


def serializer_validate(serializer):
    is_valid = serializer.is_valid()
    if not is_valid:
        log.error("SERIALIZER ERROR: %s", serializer.errors)
        raise serializers.ValidationError(serializer.errors)
    log.info("SERIALIZER DATA VALID", serializer.validated_data)


class LogingViewSet(viewsets.ViewSet):
    def create(self, request):
        """
        Register a new user.
        """
        user = request.user
        log.info("REQUEST CREATE START: %s, %s", __name__, self.__class__.__name__)
        log.info("REQUEST METHOD: %s, DATA: %s", (request.method, request.data))
        user_exists = User.objects.filter(username=dict(request.data)["username"][0])

        if (
            not user.is_authenticated
            and not user_exists
            and (request.method).lower() == "post"
        ):
            """HASHING PASSWORD"""
            old_password = request.data.get("password")
            hash = PassworHasher()
            salt = SECRET_KEY.replace("$", "/")
            hash_password = hash.hasher(old_password, salt[:50])
            """SERIALIZER DATA"""
            serializer = UserSerializer(data=request.data)
            try:
                """VALIDATE DATA"""
                serializer_validate(serializer)
                serializer.validated_data["password"] = hash_password
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

    def retrieve(self, request, pk=None):
        pass

    @action(methods=["POST"], detail=False)
    def login_user(self, request):
        """HASHING PASSWORD"""
        password = request.data.get("password")
        login = request.data.get("username")
        hash = PassworHasher()
        salt = SECRET_KEY.replace("$", "/")
        hash_password = hash.hasher(password, salt[:50])
        try:
            """CHECK EXISTS OF USER"""
            answer_bool = User.objects.filter(
                username=login, password=hash_password
            ).exists()
            if answer_bool:
                log.error("USER NOT FOUNDED")
                Response(
                    json.dumps({"data": "User not founded"}),
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            """LOGIN USER"""
            log.error("USER FOUND")
            return Response(json.dumps({"data": "User Ok"}), status=status.HTTP_200_OK)
        except Exception as ex:
            log.error("USER ERROR: %s", ex.args)
            return Response(
                json.dumps({"detail": ex.args}),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


def user_view(request):
    # form_reg =UserRegister()
    form = UserLogin()
    # form = AuthenticationForm()
    title = "Вход в аккаунт"
    if "register" in request.path.lower():
        # form = UserCreationForm()
        form = UserRegisterForm()
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
