"""
ads/urls.py
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers

from ads.views import asyncCreateAdView


# Create a router
router = DefaultRouter()
router.register("ads", asyncCreateAdView, basename="ads")

# The API URL's defined by the ads router
urlpatterns = [path("", include(router.urls))]
