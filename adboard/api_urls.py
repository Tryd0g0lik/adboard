"""
adboard/api_urls.py
"""

from rest_framework.routers import DefaultRouter

from adboard.api_views.user_views import LogingViewSet


router = DefaultRouter()
router.register("index", LogingViewSet, basename="index")
