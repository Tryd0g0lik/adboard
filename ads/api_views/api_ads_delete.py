from adrf import generics
import requests
from asgiref.sync import sync_to_async
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from adboard.api_views.token_vews import Token
from adboard.views import user_view
from ads.models import Ad
from ads.serialisers_all.ad.serializers import AdSerializer
from adrf import viewsets
from dotenv_ import POSTGRES_HOST


class AsyncAdsDelete(viewsets.GenericViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    async def destroy(self, request, pk, *args, **kwargs):
        # instance = await sync_to_async(self.get_object)()
        # user = request.user
        # cookie_token = request.COOKIES.get('token_refresh') if request.COOKIES.get('token_refresh') else request.COOKIES.get('token_access')
        token = Token()
        user_view = await token.token_get(request)
        pass
        # await instance.adelete()
        return Response(status=status.HTTP_204_NO_CONTENT)
