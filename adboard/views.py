import os
from django.shortcuts import render
from adboard.forms.register import UserRegisterForm

from adboard.forms.login import UserLogin
from project.settings import BASE_DIR
import logging
from logs import configure_logging


configure_logging(logging.INFO)
log = logging.getLogger(__name__)


def user_view(request):
    form = UserLogin()
    title = "Войдите в профиль"

    if "register" in request.path.lower():
        form = UserRegisterForm()
        title = "Регистрация"
    files = []
    # GET JS FILES FOR LOGIN AND REGISTER PAGES
    # if "login" in request.path.lower() or "register" in request.path.lower():
    files = os.listdir(f"{BASE_DIR}/collectstatic/adboard/scripts")
    files = ["adboard/scripts/" + file for file in files]

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


def main_view(request):
    title = "Добро пожаловать!"
    # GET JS FILES FOR MAIN PAGE
    files = os.listdir(f"{BASE_DIR}/collectstatic/adboard/scripts")
    files = ["adboard/scripts/" + file for file in files]

    return render(
        request,
        "index.html",
        {
            "js_files": files,
            "title": title,
        },
    )
