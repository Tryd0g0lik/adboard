import json
import pytest
import logging
from rest_framework import status
from django.core.cache import cache

from __tests__.__fixtures__.fixtures import data_random, close_all
from ads.models import Ad
from asgiref.sync import sync_to_async


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
class TestGetSingleAd:
    LIST_URL = "/api/v1/ads/"

    @pytest.mark.ad_get
    async def test_get_single_ad_valid(self, data_random, async_client, close_all):
        cache.clear()

        ads_random_list = await sync_to_async(data_random)(_quantity=2)

        response = await async_client.get(f"{self.LIST_URL}{ads_random_list[0].id}/")
        """CHECK RESPONSE - STATUS CODE"""
        assert response.status_code == status.HTTP_200_OK
        await close_all(async_client)

        data = response.json()
        data_json = json.loads(data)
        """CHECK RESPONSE - BODY"""
        assert data_json["data"][0]["title"] == ads_random_list[0].title
