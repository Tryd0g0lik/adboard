"""
adboard/urls.py
"""

# from django.contrib.auth.forms import UserCreationForm
from django.urls import path  # , include
from rest_framework.routers import DefaultRouter

from adboard.views import LogingViewSet, user_view, main_view

router = DefaultRouter()
router.register("index", LogingViewSet, basename="index")
# router.register("/api/v1/index/0/login_user", LogingViewSet, basename="login_user")
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
