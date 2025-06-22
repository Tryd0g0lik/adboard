"""
adboard/urls.py
"""

from django.urls import path

from adboard.views import user_view, main_view

urlpatterns = [
    path("", main_view, name="register_page"),
    path(
        "users/register/",
        user_view,
    ),
    path(
        "users/login/",
        user_view,
    ),
    path(
        "users/logout/",
        user_view,
    ),
]
