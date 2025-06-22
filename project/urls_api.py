from django.urls import path, include
from adboard.api_urls import router as adboard_router
from ads.api_urls import router as ads_router

urlpatterns = [
    path("users/", include((adboard_router.urls, "users_api"), "users_api")),
    path("ads/", include((ads_router.urls, "ads_api"), namespace="ads_api")),
]
