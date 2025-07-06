import base64
import json
import logging
import pickle

from rest_framework.decorators import action
from rest_framework import status
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

# from adrf import viewsets
from adrf import views, viewsets

from adboard.binaries import Binary
from logs import configure_logging
from rest_framework.permissions import AllowAny

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
response = Response(status.HTTP_401_UNAUTHORIZED)


class Token:
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

    async def token_get(self, request):
        log.info("%s: START" % Token.__class__.__name__)
        """
        This method is used for getting the user object from the token.
        """
        try:
            bytes_token: bytes

            # """GET TOKENS FROM THE HEADERS"""
            origin_token_access = request.COOKIES.get("token_access")
            origin_token_refresh = request.COOKIES.get("token_refresh")
            if not origin_token_access and not origin_token_refresh:
                raise ValueError("Invalid token")

            if origin_token_access:
                bytes_token = self.string_to_byte_tokens(origin_token_access)
            elif origin_token_refresh:
                bytes_token = self.string_to_byte_tokens(origin_token_refresh)
            # else:
            #     raise ValueError("Invalid token")
            # """GET USER ID AND USER NAME"""
            obj = pickle.loads(bytes_token)
            user_id = obj.payload["user_id"]
            user_name = obj.payload["name"]

            # Ошибка валидации
            user = await sync_to_async(User.objects.get)(
                id=int(user_id), username=user_name
            )
            # """RECEIVE THE USER OBJECT AS BINARY DATA"""

            # log.info("%s: Here is all OK at the %s" % (Token.__class__.__name__, self.token_get.__name__))
            return user
        except Exception as e:
            message = "%s: %s ERROR: %s" % (
                Token.__class__.__name__,
                self.token_get.__name__,
                e.__str__(),
            )
            raise ValueError(message)
