""""
ads/api_views/api_ads.py
"""

import json
import logging
from asgiref.sync import sync_to_async
from django.http import JsonResponse

from ads.api_views.api_files import async_serializer_validate
from ads.serialisers_all.ad.serializers import AdSerializer
from logs import configure_logging
from django.shortcuts import redirect
from rest_framework import status

from adrf import viewsets
from rest_framework.response import Response

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad, ImageStorage
from project.tokens import TokenResponse

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START")


response = Response(
    status=status.HTTP_401_UNAUTHORIZED,
)


class AsyncAdsView(viewsets.ModelViewSet):
    """ASYNC CREATE AD"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    async def list(self, request, *args, **kwargs):
        """
        This шs method for sending all ads for user if this user is author and is authenticated.\
        Superuser user (is authenticated) can get all ads.
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': [{}, {}, ...]}`
        """
        user = request.user
        try:
            """CHECK USER TOKEN"""
            tokens = TokenResponse(self.request)
            response = tokens.tokens_response
            if response.status_code == status.HTTP_401_UNAUTHORIZED:
                return response
        except Exception as er:
            log.exception("ERROR => %s", er)
            return redirect(to="/users/login/")

        if not user.is_anonymous:
            try:
                response = await sync_to_async(super().list)(request, *args, **kwargs)
                data = [ad for ad in response.data if ad["user"] == user.id]
                if user.is_superuser == True:
                    data = [ad for ad in response.data]
                response.data = json.dumps({"data": data})
                return response
            except Exception as ex:
                response = JsonResponse(
                    json.dumps({"detail": [ex.args]}),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
                return response
        return JsonResponse(
            json.dumps({"detail": ["User is not authenticated."]}),
            status=status.HTTP_401_UNAUTHORIZED,
        )

    async def retrieve(self, request, *args, **kwargs):
        """
        This is method for getting/opening the information about one ad
        :param request:
        :param pk:
        :return: json string this is `{'data': {}}`
        """
        user = request.user
        data: object
        try:
            """CHECK USER TOKEN"""
            tokens = TokenResponse(self.request)
            response = tokens.tokens_response
            if response.status_code == status.HTTP_401_UNAUTHORIZED:
                return response
        except Exception as er:
            log.exception("ERROR => %s", er)
            return redirect(to="/users/login/")

        if not user.is_anonymous and not kwargs["pk"] == "undefined":
            try:
                response = await sync_to_async(super().retrieve)(
                    request, int(kwargs["pk"])
                )
                data = Response(
                    json.dumps({"data": [dict(response.data)]}),
                    status=status.HTTP_200_OK,
                )
            except Exception as ex:
                data = JsonResponse(
                    json.dumps({"detail": [ex.args]}),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            finally:
                return data
        return Response(
            json.dumps({"detail": ["User is not authenticated or pk is undefined."]}),
            status=status.HTTP_401_UNAUTHORIZED,
        )

    async def create(self, request, *args, **kwargs):
        """
        This is method for creating a new ad.
        From request will be checking the: \
        - user's authenticated; \
        - user's tokens and if we have only everything is correct the new ad will be added.
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': {}}`
        """
        log.info("START CREATE of VIEWS.py")
        log.info("REQUEST DATA: %s", request.data)
        """GET USER"""
        request_user = request.user
        """CHECK USER TOKEN"""
        try:
            tokens = TokenResponse(self.request)
            response = tokens.tokens_response
            if response.status_code == status.HTTP_401_UNAUTHORIZED:
                return response
        except Exception as er:
            log.exception("ERROR => %s", er)

            return redirect(to="/users/login/")
        if not request_user.is_anonymous:
            """GET USER IN DATA FOR SERIALIZATION"""
            data = {
                "user": request.user.pk,
                "title": request.data["title"],
                "description": request.data["description"],
                "category": request.data["category"],
                "condition": request.data["condition"],
                "path": request.data["path"],
            }
            serializer = self.get_serializer(data=data)
            try:
                await async_serializer_validate(serializer)
                log.info("AD IS VALIDATED DATA:")
            except Exception as er:
                log.error("AD SERIALIZER DATA ERROR: %s", er)
                response.data = json.dumps(
                    {"detail": "AD serializer data error. %s" % er.args}
                )
                return response
            try:
                await sync_to_async(self.perform_create)(serializer)
                log.info("SERIALIZER DATA SAVED")
                response.data = json.dumps({"data": serializer.data})
                response.status_code = status.HTTP_201_CREATED
                return response
            except Exception as e:
                log.exception("ERROR => %s", e)
                response.data = {"detail": "Server error: %s" % e}
                response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
                return response
        response.data = {"detail": ["User is not authenticated. New ad is not saved. "]}
        return response
