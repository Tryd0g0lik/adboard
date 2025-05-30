"""
ads/urls.py
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers

from ads.views import AsyncAdsView, FileImageViewSet

app_name = "ads_app"

router = DefaultRouter()
router.register("ads", AsyncAdsView, basename="ads")

router.register("image", FileImageViewSet, basename="image")

# The API URL's defined by the ads router
urlpatterns = [
    path("", include((router.urls, "c"), namespace="ads_api")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
