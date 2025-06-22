""""
ads/views.py
"""

import os
import logging
from logs import configure_logging
from project.settings import BASE_DIR
from django.shortcuts import render, redirect
from rest_framework import status

from ads.forms.ad_creat import adCreatForm, FileImageForm
from project.tokens import TokenResponse

configure_logging(logging.INFO)
log = logging.getLogger(__name__)
log.info("START")


def ads_page(request):
    theme = request.GET.get("theme", "dark")

    try:
        """CHECK USER TOKEN"""
        tokens = TokenResponse(request)
        response = tokens.tokens_response
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            return response
    except Exception as er:
        log.exception("ERROR => %s", er)
        return redirect(to="/users/login/")
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
    if request.method == "GET":
        try:
            """CHECK USER TOKEN"""
            tokens = TokenResponse(request)
            response = tokens.tokens_response
            if response.status_code == status.HTTP_401_UNAUTHORIZED:
                return response
        except Exception as er:
            log.exception("ERROR => %s", er)
            return redirect(to="/users/login/")
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
