""""
ads/views.py
"""

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from adrf.viewsets import ViewSet

from ads.forms.ad_creat import adCreatForm

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad
from ads.serializers import AdSerializer


# Create your views here.


class asyncCreateAdView(ViewSet):
    ads = Ad.objects.all()
    serializer_class = AdSerializer


def main_page(request):
    # Forms
    form = adCreatForm()
    return render(request, template_name="index.html", context={"form": form})
