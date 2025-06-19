"""
ads/urls.py
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter


# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers

from ads.views import AsyncAdsView, FileImageViewSet
from ads.views import ads_page, ad_page

app_name = "ads_app"

router = DefaultRouter()
router.register("index", AsyncAdsView, basename="ads")

router.register("image", FileImageViewSet, basename="image")

# The API URL's defined by the ads router
urlpatterns = [
    # path("", include(router.urls)),
    path("", ads_page, name="ads_url"),  # !!!!!!!!! URL НА ФРОНТЕ
    path("ad/<str:pk>/", ad_page, name="ad_url"),  # !!!!!!!!! URL НА ФРОНТЕ
]
