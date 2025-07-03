from adrf import generics

from ads.models import Ad
from ads.serialisers_all.ad.serializers import AdSerializer


class AsyncAdsDelete(generics.DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    # async def get_extra_actions(self):
    #     return
    async def destroy(self, request, *args, **kwargs):
        pass
        # if request.user.is_authenticated:
        #     pass
        # else:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        return self.destroy(request, *args, **kwargs)
