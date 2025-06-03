"""
adboard/urls.py
"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from adboard.views import LogingViewSet, user_view

router = DefaultRouter()
router.register("index", LogingViewSet, basename="index")
# router.register("index/0/login_user", LogingViewSet, basename="login_user")
urlpatterns = [
    path("", user_view, name="register_page"),
    path(
        "register/",
        user_view,
    ),
    path(
        "login/",
        user_view,
    ),
]
