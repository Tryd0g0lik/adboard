from django.urls import path, include
from adboard.urls import router as adboard_router
from weather.urls import router as weather_router
from ads.urls import router as ads_router

urlpatterns = [
    path(
        "weather/",
        include((weather_router.urls, "weather_api"), namespace="weather_api"),
    ),
    path("users/", include((adboard_router.urls, "users_api"), "users_api")),
    path("ads/", include((ads_router.urls, "ads_api"), namespace="ads_api")),
]
