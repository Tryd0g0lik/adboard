""""
ads/views.py
"""

import json
import os
import logging
import time
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from django.http import JsonResponse

from adboard.views import LogingViewSet
from ads.serialisers_all.ad.serializers import AdSerializer
from ads.serialisers_all.imageStorage.serializers import ImageStorageSerializer
from logs import configure_logging
from project.settings import BASE_DIR, SIMPLE_JWT
from django.shortcuts import render
from rest_framework import status

# from rest_framework import views, generics, viewsets, decorators
from adrf import viewsets
from rest_framework.response import Response


from ads.forms.ad_creat import adCreatForm, FileImageForm

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad, ImageStorage
from project.tokens import TokenRequest

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START")


# Create your views here.
async def async_serializer_validate(serializer):
    """
    Async validation of serializer.
    """
    is_valid = await sync_to_async(serializer.is_valid)()
    if not is_valid:
        log.error("SERIALIZER ERROR: %s", serializer.errors)
        raise ValidationError(serializer.errors)
    log.info("SERIALIZER DATA VALID: %s", serializer.validated_data)
    data = await sync_to_async(lambda: serializer.validated_data)()
    return data


class FileImageViewSet(viewsets.ModelViewSet):
    """IMAGE STORAGE"""

    queryset = ImageStorage.objects.all()
    serializer_class = ImageStorageSerializer

    async def create(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': {}}`
        """
        """SAVE IMAGE FILE"""
        log.info("START CREATE IMAGE")
        log.info("REQUEST DATA: %s", request.data)
        request.data["size"] = request.data["file_path"].size
        serializer = self.get_serializer(data=request.data)
        try:
            """VALIDATE DATA"""
            await async_serializer_validate(serializer)
        except Exception as er:
            log.error("IMAGE SERIALIZER DATA IS NOT VALID: %s", er)
            return Response(
                json.dumps({"detail": er.args}), status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            await sync_to_async(self.perform_create)(serializer)
            log.info("SERIALIZER DATA SAVED: %s", serializer.data)
            return Response(
                data=json.dumps({"data": serializer.data}),
                status=status.HTTP_201_CREATED,
            )
        except Exception as ex:
            log.error("NEW IMAGE_FILE SERVER ERROR: %s", ex)
            return JsonResponse(
                {"detail": ex.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AsyncAdsView(viewsets.ModelViewSet):
    """ASYNC CREATE AD"""

    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    async def list(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return: json string this is `{'data': [{}, {}, ...]}`
        """
        user = request.user
        data: object
        if not user.is_anonymous:
            try:
                data = await sync_to_async(super().list)(request, *args, **kwargs)
                data.data = json.dumps({"data": data.data})
            except Exception as ex:
                data = JsonResponse(
                    json.dumps({"detail": [ex.args]}),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            finally:
                return data
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
        tokens = TokenRequest(request)
        number = tokens.tokens_check
        """TEMPLATE RESPONSE FOR RETURNING"""
        response = Response(
            status=status.HTTP_401_UNAUTHORIZED,
        )
        response_render = Response(
            render(tokens.request, "index.html", status=status.HTTP_401_UNAUTHORIZED)
        )
        """CHECK TOKEN"""
        try:
            if number == 1:
                """TOKENS IS PROVIDED OR IS REFRESH AND SAVE TO THE COOKIE"""
                response = tokens.token_refresh
            if number == 2:
                """TOKENS IS NOT PROVIDED"""
                response_render.content = ({"detail": ["Token is not provided."]},)
                tokens._change_user_active(active=False)
                return response_render
        except Exception as error:
            """USER NOT FOUND IN DB"""
            response_render.content = {
                "detail": ["User not founded щк token is error.%s" % error]
            }
            return response_render
        if not request_user.is_anonymous:

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
                response.status = status.HTTP_201_CREATED
                return response
            except Exception as e:
                log.exception("ERROR => %s", e)
                response.data = {"detail": "Server error: %s" % e}
                response.status = status.HTTP_500_INTERNAL_SERVER_ERROR
                return response
        response.data = {"detail": ["User is not authenticated. New ad is not saved. "]}
        return response


def ads_page(request):
    theme = request.GET.get("theme", "dark")
    # GET JS FILES FOR LOGIN AND REGISTER PAGES
    files = os.listdir(f"{BASE_DIR}/collectstatic/ads/scripts")
    files = ["ads/scripts/" + file for file in files]
    css_file = "styles/index.css"
    if theme == "lite":
        css_file = "styles/lite.css"

    # Forms
    form = adCreatForm()
    file_image = FileImageForm()
    return render(
        request,
        template_name="ads/index.html",
        context={
            "form": {"forms_main": form, "file_image": file_image},
            "css_file": css_file,
            "js_files": files,
        },
    )


def ad_page(request, *args, **kwargs):
    pass
    if request.method == "GET":
        # files = os.listdir(f"{BASE_DIR}/ads/static/"
        files = os.listdir(f"{BASE_DIR}/collectstatic/ads/scripts")
        files = ["ads/scripts/" + file for file in files]
        # // files = os.listdir(f"{BASE_DIR}/collectstatic/scripts")
        css_file = "styles/index.css"
        # data_str = json.dumps({"data": response})
        return render(
            request,
            template_name="ad/index.html",
            context={
                "css_file": css_file,
                "js_files": files,
            },
        )
