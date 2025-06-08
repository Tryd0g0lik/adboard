from rest_framework.routers import DefaultRouter
from weather.views import WeatherViewSet, weather_view
from django.urls import path

router = DefaultRouter()
router.register("index", WeatherViewSet, basename="index")

urlpatterns = [
    path("", weather_view, name="weather"),
]
