""""
ads/views.py
"""

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from adrf.viewsets import ViewSet

from ads.forms.ad_creat import adCreatForm

# https://socket.dev/pypi/package/adrf
# https://socket.dev/pypi/package/adrf
from ads.models import Ad
from ads.serializers import AdSerializer


# Create your views here.


class asyncCreateAdView(ViewSet):
    # ads = Ad.objects.all()
    # serializer_class = AdSerializer

    async def list(self, request):
        queryset = Ad.objects.all()
        serializer = AdSerializer(queryset, many=True)
        if serializer.is_valid():
            return Response(request, serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                request, serializer.data, status=status.HTTP_401_UNAUTHORIZED
            )

    async def create(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request, serializer.data, status=status.HTTP_200_OK)


def main_page(request):
    theme = request.GET.get("theme", "dark")
    if theme == "dark":
        css_file = "styles/index.css"
    # Forms
    form = adCreatForm()
    # if request.method == 'POST':
    #     form_data = adCreatForm(request.POST)
    #     pass
    #     if not form_data.is_valid():
    #        pass
    return render(
        request,
        template_name="index.html",
        context={"form": form, "css_file": css_file},
    )
