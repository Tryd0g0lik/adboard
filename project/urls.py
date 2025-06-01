"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from ads.urls import urlpatterns as ads_urls
from ads.views import main_page, ad_page
from adboard.urls import router, urlpatterns as user_urls
from weather.urls import router as weather_router, urlpatterns as weather

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/v1/", include((ads_urls, "ads_api"), namespace="ads_api")),
    path("ad/<str:pk>/", ad_page, name="ad_api"),
    path("users/", include((user_urls, "users_url"), "users_url")),
    path("api/v2/", include((router.urls, "app_users"), "users_api")),
    path("weather/", include((weather, "weather_url"), namespace="weather_url")),
    path(
        "api/v1/weather/",
        include((weather_router.urls, "weather_api"), namespace="weather_api"),
    ),
    path("", main_page, name="main"),
]
