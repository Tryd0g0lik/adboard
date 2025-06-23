"""
ads/api_urls.py
"""

from rest_framework.routers import DefaultRouter

# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
from ads.api_views.api_ads import AsyncAdsView
from ads.api_views.api_files import FileImageViewSet


app_name = "ads_app"

router = DefaultRouter()
router.register("index", AsyncAdsView, basename="ads")
router.register("image", FileImageViewSet, basename="image")
