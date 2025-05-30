from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.utils.translation import gettext_lazy as _

# Create your models here.


class WeatherForecast(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
    )
    latitude = models.FloatField(
        max_length=7,
        blank=True,
        help_text=_("latitude for forecast"),
        validators=[
            MaxLengthValidator(
                7, message=_("Maximum quantity of symbols before 7 symbols/characters")
            ),
            MinLengthValidator(
                2, message=_("Minimum quantity of symbols is 2 symbols/characters")
            ),
        ],
    )
    longitude = models.FloatField(
        max_length=7,
        blank=True,
        help_text=_("longitude for forecast"),
        validators=[
            MaxLengthValidator(
                7, message=_("Maximum quantity of symbols before 7 symbols/characters")
            ),
            MinLengthValidator(
                2, message=_("Minimum quantity of symbols is 2 symbols/characters")
            ),
        ],
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("Date when user is last time used the service"),
    )

    def __str__(self):
        return "Latitude: %s. Longitude: %s" % (self.latitude, self.longitude)

    class Meta:
        db_table = "weather"
        verbose_name = _("weather")
        verbose_name_plural = _("weathers")
