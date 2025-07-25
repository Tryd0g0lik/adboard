import base64
import json
import pickle
import time
import logging
from datetime import datetime
from typing import Dict, Optional, TypeVar

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib.auth import authenticate, login
from asgiref.sync import sync_to_async
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import TokenUser
from rest_framework import serializers, status
from adrf.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from adboard.binaries import Binary
from adboard.hasher import PassworHasher
from adboard.serializers.register import UserSerializer
from logs import configure_logging
from project.settings import SECRET_KEY, SIMPLE_JWT

configure_logging(logging.INFO)
log = logging.getLogger(__name__)


def serializer_validate(serializer):
    is_valid = serializer.is_valid()
    if not is_valid:
        log.error("SERIALIZER ERROR: %s", serializer.errors)
        raise serializers.ValidationError(serializer.errors)
    log.info("SERIALIZER DATA VALID", serializer.validated_data)


class LogingViewSet(ViewSet):
    AuthUser = TypeVar("AuthUser", AbstractBaseUser, TokenUser)

    # permission_classes = [IsAuthenticated]

    @staticmethod
    def _jwt_user_checker(token: Optional[str], user_object: User) -> None:
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

    @classmethod
    def async_token_refresh(cls, user_object):
        try:
            tokens = LogingViewSet._jwt_user_refresh(user_object)
            return tokens
        except Exception as ex:
            raise ValueError("Error 4s" % ex)

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
        password_hash = self.get_hash_password(request.data.get("password"))
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
        hash_password = self.get_hash_password(request.data.get("password"))
        """CHECK EXISTS OF USER"""
        user_one_list = await sync_to_async(User.objects.filter)(
            username=login_user, password=hash_password
        )
        user_one = await sync_to_async(user_one_list.first)()

        if not user_one:
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
        try:
            user_one.last_login = datetime.now()
            """SAVE USER"""
            await sync_to_async(user_one.save)()
            tokens = await self.async_token(user_one)
            """ ИЗМЕНИТЬ ВРЕМЯ"""
            current_time = datetime.now()
            access_time = (SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]).seconds
            refresh_time = (
                SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"] + current_time
            ).timestamp() - time.time()

        except Exception as ex:
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
        user: object
        if request.user.is_authenticated:
            try:
                user = await self.get_user_from_token(request)
                if not user:
                    return redirect("main", status=status.HTTP_401_UNAUTHORIZED)

            except Exception:
                user = request.user
                user.is_active = False
                await sync_to_async(user.save)()
                return redirect("main", status=status.HTTP_401_UNAUTHORIZED)

            if not user.is_active:
                return redirect("main")
            try:
                user.is_active = False
                await sync_to_async(user.save)()
                return Response(
                    {"data": "User logout successful"}, status=status.HTTP_200_OK
                )
            except Exception as ex:
                return Response(
                    {"detail": f"error {ex}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return redirect("main", status=status.HTTP_401_UNAUTHORIZED)

    async def get_user_from_token(self, request):
        """
        This method is used for getting the user object from the token.
        """
        try:
            bytes_token: bytes

            """GET TOKENS FROM THE HEADERS"""
            origin_token_access = request.COOKIES.get("token_access")
            origin_token_refresh = request.COOKIES.get("token_refresh")
            if not origin_token_access and not origin_token_refresh:
                raise ValueError("Invalid token")

            if origin_token_access:
                bytes_token = self.string_to_byte_tokens(origin_token_access)
            elif not origin_token_refresh:
                bytes_token = self.string_to_byte_tokens(origin_token_refresh)

            """GET USER ID AND USER NAME"""
            obj = pickle.loads(bytes_token)
            user_id = obj.payload["user_id"]
            user_name = obj.payload["name"]
            user = await sync_to_async(User.objects.get)(
                id=int(user_id), username=user_name
            )

            return user
        except Exception as e:
            raise AuthenticationFailed(f"Invalid token: {e}")

    @staticmethod
    def string_to_byte_tokens(string: str) -> bytes:
        """
        This method for converting from string to bytes
        :param string: string for convert to bytes
        :return: byte string
        """
        try:
            byte_string = base64.b64decode(string)
            return byte_string
        except Exception as ex:
            raise ValueError(f"Error converting to bytes: {ex}")

    @staticmethod
    def get_hash_password(password):
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
