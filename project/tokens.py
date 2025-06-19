import time
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render

from adboard.views import LogingViewSet
from rest_framework import status
from rest_framework.response import Response

from project.settings import SIMPLE_JWT


class UserActiveMixin:
    """
    This method gets and returns the user from db or errors if user is not founded.
    :return: user object or error
    """

    def __init__(self, request):
        """
        This is constructor.
        :param request: request object
        """
        self.request = request
        self.request_user = request.user

    def __get_user_db(self):
        """
        This method gets and returns the user from db or errors if user is not founded.
        :return: user object or error
        """
        cl = __class__.__name__
        try:
            """SEARCH USER IN DB"""
            request_user_id: int = self.request_user.id
            user = User.objects.filter(id=request_user_id).first()
            if not user:
                """USER IS NOT FOUND"""
                raise ValidationError(
                    "%s: user is not founded." % cl.__get_user_db.__name__
                )
            return user
        except Exception as error:
            cl = __class__.__name__
            raise ValidationError(
                "%s: user is invalid. %s" % (cl.__get_user_db.__name__, error)
            )

    @property
    def user(self):
        """
        This method gets and returns the user from db or errors if user is not founded.
        :return: user object or error
        """
        cl = __class__.__name__
        try:
            user = self.__get_user_db()
            return user
        except Exception as error:
            raise ValidationError("%s: %s" % (cl.__get_user_db.__name__, error))


class TokenResponse(UserActiveMixin):
    """
    This is for getting the token from the request.
    """

    def __init__(self, request):
        """
        This is constructor.
        :param request: request object
        """
        super().__init__(request)
        cl = __class__.__name__
        if request.user.is_authenticated:
            self._token_access = request.COOKIES.get("token_access")
            self._token_refresh = request.COOKIES.get("token_refresh")
        else:
            """USER I+S NOT AUTHENTICATED"""
            raise ValidationError(
                "%s: user is not authenticated." % cl.__init__.__name__
            )

    def _change_user_active(self, active: bool = False) -> bool:
        """
        This method changes user status of active.
        :param active: boolian to change status of user. If it is true it means user is active.\
        If it is false it means user is not active.
        :return: True if status was changed. Otherwise, error.
        """
        user: object
        cl = __class__.__name__
        try:
            user = self.user
        except Exception as error:
            """USER FROM DB IS ERROR"""
            raise ValidationError("%s: User not founded. %s" % (cl, error))
        user.is_active = active
        user.save()
        return True

    @property
    def tokens_check(self) -> int:
        """
        0 - token is provided.\
        1 - token_refresh is not provided and token_access is provided.\
        2 - tokens is not provided
        This method checks the tokens.
        :return: int
        """
        if self._token_refresh:
            return 0
        elif self._token_access and not self._token_refresh:
            return 1
        return 2

    @property
    def token_refresh(self) -> Response:
        """
        This method returns the token refresh. If the token is not provided od user invalid, it returns the 401.
        :return: Response
        """
        user: object

        user = self.user
        try:
            """TOKEN REFRESH"""
            tokens = LogingViewSet.async_token_refresh(user)
            current_time = datetime.now()
            """UPDATE TIME OF TOKEN's LIFE """
            refresh_time = (
                SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"] + current_time
            ).timestamp() - time.time()
            response = Response(
                {"detail": ["Token is not provided."]},
                status=status.HTTP_201_CREATED,
            )
            response.set_cookie(
                "token_access", tokens["token_access"], max_age=refresh_time
            )
            return response
        except Exception as error:
            """TOKEN REFRESH NOT VALID"""
            self._change_user_active(active=False)
            raise ValidationError(
                "%s:Token refresh not valid %s" % (__class__.__name__, error)
            )

    @property
    def tokens_response(self):
        """
        This method returns the status code 401, it means that the response has not provided tokens or \
        tokens are invalid and rendering to the main page.
        If method returns the status code 201, it means that the token_access was updated or all ok.
        :return: Response
        Example: '''py
                try:
            tokens = TokenResponse(self.request)
            response = tokens.tokens_response
            if response.status_code == status.HTTP_401_UNAUTHORIZED:
                return response
        except Exception as er:
            log.exception("ERROR => %s", er)
            response.data = json.dumps({"detail": "Something went wrong."})
            return response
        '''
        """
        number = self.tokens_check
        """TEMPLATE RESPONSE FOR RETURNING"""

        response_render = Response(
            render(self.request, "index.html", status=status.HTTP_401_UNAUTHORIZED)
        )
        """CHECK TOKEN"""
        try:
            if number == 1:
                """TOKENS IS PROVIDED OR IS REFRESH AND SAVE TO THE COOKIE"""
                return self.token_refresh
            if number == 2:
                """TOKENS IS NOT PROVIDED"""
                response_render.content = ({"detail": ["Token is not provided."]},)
                self._change_user_active(active=False)
                return response_render
            response_render.status_code = status.HTTP_201_CREATED
            return response_render
        except Exception as error:
            """USER NOT FOUND IN DB"""
            response_render.content = {
                "detail": ["User not founded щк token is error.%s" % error]
            }
            return response_render
