"""
ads/urls.py
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers

from ads.views import AsyncCreateAdView, FileImageViewSet

# Create a router
router = DefaultRouter()
router.register("ads", AsyncCreateAdView, basename="ads")
router.register("image", FileImageViewSet, basename="image_file")

# The API URL's defined by the ads router
urlpatterns = [
    path("", include(router.urls)),
]
