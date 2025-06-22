"""
ads/urls.py
"""

from django.urls import path
from ads.views import ads_page, ad_page


# The API URL's defined by the ads router
urlpatterns = [
    path("", ads_page, name="ads_url"),  # !!!!!!!!! URL НА ФРОНТЕ
    path("ad/<str:pk>/", ad_page, name="ad_url"),  # !!!!!!!!! URL НА ФРОНТЕ
]
