"""
adboard/urls.py
"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from adboard.views import UserViewSet, registration_view

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", registration_view, name="register_page"),
    path(
        "register/",
        registration_view,
    ),
    path(
        "login/",
        registration_view,
    ),
]
