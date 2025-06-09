import json
import os

# import requests
from datetime import datetime
from typing import Dict, Optional, TypeVar


from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.serializers import TokenVerifySerializer

# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import TokenUser

# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from adboard.binaries import Binary
from adboard.forms.register import UserRegisterForm

from adboard.forms.login import UserLogin
from adboard.hasher import PassworHasher
from adboard.serializers.register import UserSerializer
from project.settings import BASE_DIR, SECRET_KEY
import logging
from rest_framework import serializers, status  # viewsets,
from adrf.viewsets import ViewSet
from rest_framework.response import Response

from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib.auth import authenticate, login
from logs import configure_logging
from project.settings import SIMPLE_JWT

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


class LogingViewSet(ViewSet):
    # permission_classes = [IsAuthenticated]
    AuthUser = TypeVar("AuthUser", AbstractBaseUser, TokenUser)

    @staticmethod
    def _jwt_user_checker(token: Optional[str], user_object: type(User)) -> None:
        """
        Checking user is owner of this token or not.
        If user is not owner of this token then raise error.
        :param token: jwt access token.
        :param user_object: user object.
        :return None
        """
        if not token or not user_object:
            raise ValueError("Check your data")
        access_tokeen = AccessToken(token)
        user_id: int = access_tokeen["user_id"]
        if user_object.get("id") != user_id:
            raise ValueError("User is not owner of this token.")

    @classmethod
    async def async_token(cls, user_object: AuthUser):
        """
        This is method for getting token for user.
        :param user_object: This is a user's object for a which will be token generating \
        :return: this dictionary with 4 values
        :return: {
                {"token_access": "< access_token >", "live_time": "< life_time_of_token >"},
                {"token_refresh": "< refresh_token >", "live_time": "< life_time_of_token >"}
            }
        """

        tokens = await cls.__async_generate_jwt_token(user_object)
        return tokens

    @staticmethod
    async def __async_generate_jwt_token(user_object: AuthUser) -> {Dict[str, str]}:
        """
            Only, after registration user we will be generating token for \
            user through 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer'
            This is a generator token of user.\
            The 'SIMPLE_JWT' is variable from the project's 'settings.py' file.\
            @SIMPLE_JWT.ACCESS_TOKEN_LIFETIME this is minimum quantity for life of token\
             It is for the access.\
            @REFRESH_TOKEN_LIFETIME this is maximum quantity fro life token. \
            It is for the refresh.
            'TokenObtainPairSerializer' it has own db/
            :return:
        """
        """TIME TO THE LIVE TOKEN"""
        # dt = datetime.datetime.now() + datetime.timedelta(days=1)
        """GET TOKEN"""
        try:
            token = TokenObtainPairSerializer.get_token(user_object)
            token["name"] = (lambda: user_object.username)()
            return token
        except Exception as ex:
            raise ValueError("Value Error: %s" % ex)

    @staticmethod
    def _jwt_user_refresh(item: AuthUser) -> Dict[str, str]:
        """
        Refresh token.
        :param item: User object or token object.
        """
        refresh = RefreshToken.for_user(item)
        return {
            "token_access": str(refresh.access_token),
            "token_refresh": str(refresh),
        }

    def retrieve(self, request, pk=None):
        pass

    def create(self, request) -> type(Response):
        """CHECK USER DATA"""
        user = request.user
        password_hash = self.hash_password(request.data.get("password"))
        log.info("PASSWORD HASH: %s", password_hash)
        """CHECK USER EXISTS"""
        user_list = User.objects.filter(username=request.data.get("username"))

        log.info("USER EXISTS: %s", user_list.exists())
        if not user.is_authenticated and not user_list.exists():
            try:
                serializer = UserSerializer(data=request.data)
                serializer_validate(serializer)
                serializer.validated_data["password"] = password_hash
                serializer.save()
                log.info("USER CREATED SUCCESSFUL")
                return Response(
                    {"data": "USER CREATED"}, status=status.HTTP_201_CREATED
                )

            except Exception as ex:
                log.error("SERIALIZER DATA ERROR: %s", ex.args)
                return Response(
                    {"detail": ex.args}, status=status.HTTP_401_UNAUTHORIZED
                )
        log.error("USER NOT CREATED")
        return Response(
            json.dumps({"detail": "USER NOT CREATED"}),
            status=status.HTTP_401_UNAUTHORIZED,
        )

    @action(methods=["POST"], detail=True)
    async def login_user(self, request, pk: str = "0"):
        """
        "/api/v1/index/0/login_user"
        This method is used the user's login and IP ADDRESS of client.
        Here, If we have the object of user , it means we will  get token objects for user.
        "token_access" - it is general token of user for access to the service.
        "token_refresh" - it is token for refresh the access token.
        :param request:
        :param pk: not used. It is just for URL.
        :return: ```js
        {"data":[
                    {
                        "token_access": str( < access_token >),
                        "live_time": < lifetime_from_minutes >,
                    },
                    {
                        "token_refresh": str(tokens),
                        "live_time": < lifetime_from_hours >,
                    },
                ]}
                ````
        """

        password = request.data.get("password")
        login_user = request.data.get("username")
        """HASH PASSWORD OF USER"""
        hash_password = self.hash_password(request.data.get("password"))
        """CHECK EXISTS OF USER"""
        user_one_list = await sync_to_async(User.objects.filter)(
            username=login_user, password=hash_password
        )
        user_one = await sync_to_async(user_one_list.first)()

        if not user_one:
            log.error("USER NOT FOUNDED")
            return Response(
                {"data": "User not founded"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        """GET USER DATA"""
        user_one.is_active = True
        """SAVE USER"""
        await sync_to_async(user_one.save)()
        """GET AUTHENTICATION (USER SESSION) IN DJANGO """
        user = await sync_to_async(authenticate)(
            request, username=login_user, password=password
        )
        if user is not None:
            await sync_to_async(login)(request, user)
        else:
            log.error("USER NOT FOUNDED")
            return Response(
                {"data": "User not founded"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        """GET LOCATION OF USER"""
        # user_ip_address = request.META.get("REMOTE_ADDR")  # Не трогать - используется
        try:
            # response = await sync_to_async(requests.post)(
            #     "http://ip-api.com/batch",
            #     data=json.dumps(
            #         [
            #             {ПОГОДА
            #                 "query": user_ip_address,  # "83.166.245.197",  # Изменить на user_ip_address
            #                 "fields": ["lat", "lon"],  # Исправлено на lat/lon
            #                 "lang": "ru",
            #             }
            #         ]
            #     ),
            # )
            # response = response.json()
            # """GET LOCATION BASIS/INITIAL"""
            # latitude: float = response[0]["lat"]
            # longitude: float = response[0]["lon"]
            # log.info("LATITUDE OF USER: %s", latitude)
            # user_one.latitude = latitude
            # user_one.longitude = longitude
            user_one.last_login = datetime.now()
            """SAVE USER"""
            await sync_to_async(user_one.save)()

            log.info("USER IS ACTIVE: %s", user_one.is_active)
            tokens = await self.async_token(user_one)
            log.info("USER TOKEN IS ACTIVE: %s", str(tokens))
            """ ИЗМЕНИТЬ ВРЕМЯ"""
            access_time = (SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]).total_seconds() * 1000
            refresh_time = SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds() * 1000

        except Exception as ex:
            log.error("USER ERROR: %s", ex.args)
            return Response({"detail": ex.args}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            """ACCESS TOKEN BASE64"""
            access_binary = Binary()
            access_base64_str = access_binary.object_to_binary(tokens.access_token)
            access_result = access_binary.str_to_binary(access_base64_str)
            """ REFRESH TOKEN BASE64"""
            reffresh_binary = Binary()
            reffresh_base64_str = reffresh_binary.object_to_binary(tokens)
            reffresh_result = reffresh_binary.str_to_binary(reffresh_base64_str)
            return JsonResponse(
                {
                    "data": [
                        {
                            "token_access": access_result,
                            "live_time": access_time,
                        },
                        {
                            "token_refresh": reffresh_result,
                            "live_time": refresh_time,
                        },
                    ]
                },
                status=status.HTTP_200_OK,
            )
        except Exception as ex:
            log.error("USER's TOKENS IS ERROR: %s", ex.args)
            return Response(
                {"detail": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(methods=["GET"], detail=True)
    async def logout_user(self, request, pk: str = "0"):
        """
        "/api/v1/users/index/0/logout_user"
        This method is used for logout user.
        :param request:
        :param pk:
        :return:
        """

        # request_user = await sync_to_async(lambda:  request.user)()
        self.get_user_from_token(request)
        # if not await sync_to_async(lambda: request_user.is_authenticated)():
        #     return Response({"data": "User have not logged in"},
        #                    status=status.HTTP_401_UNAUTHORIZED)
        return Response({"data": "User logout successful"}, status=status.HTTP_200_OK)

    @staticmethod
    def get_user_from_token(request):
        try:
            # Извлекаем пользователя из токена
            auth = JWTAuthentication()
            header = auth.get_header(request)  # Получаем заголовок Authorization
            raw_token = auth.get_raw_token(header)  # Извлекаем токен
            validated_token = auth.get_validated_token(raw_token)  # Валидируем
            user = auth.get_user(validated_token)  # Получаем пользователя
            return user
        except Exception as e:
            raise AuthenticationFailed("Invalid token")

    @staticmethod
    def hash_password(password):
        """
        This method for hashing user password.
        :param password: Password of user before hashing (from request)
        :return: password hashed
        """
        """HASH PASSWORD OF USER"""
        hash = PassworHasher()
        salt = SECRET_KEY.replace("$", "/")
        hash_password = hash.hasher(password, salt[:50])
        return hash_password


def user_view(request):
    form = UserLogin()
    title = "Вход в аккаунт"

    if "register" in request.path.lower():
        form = UserRegisterForm()
        title = "Регистрация"
    files = []
    # GET JS FILES FOR LOGIN AND REGISTER PAGES
    if "login" in request.path.lower() or "register" in request.path.lower():
        files = os.listdir(f"{BASE_DIR}/collectstatic/adboard/scripts")
        files = ["adboard/scripts/" + file for file in files]
        title = "Авторизация"

    return render(
        request,
        "users/index.html",
        {
            "js_files": files,
            "form": {
                "form_user": form,
            },
            "title": title,
        },
    )
