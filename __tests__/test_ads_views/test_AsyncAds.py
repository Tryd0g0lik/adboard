"""
__tests__/test_ads_views/test_AsyncAds.py

Here we test 'Ad' model for creating new line of ad
"""

import json
from __tests__.__fixtures__.fixtures import (
    test_Ad_valid,
    data_random,
    async_client,
    close_all,
)
import logging
import pytest

from rest_framework import status
from django.core.cache import cache
from asgiref.sync import sync_to_async


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
class TestAd:
    """Test for Ad creating"""

    LIST_URL = "/api/v1/ads/"

    @pytest.mark.ad_create
    async def test_create_ad_valid(
        self,
        close_all,
        async_client,
        test_Ad_valid,
    ):
        # Arrange
        """CREATE AD"""
        cache.clear()

        # Act
        response = await sync_to_async(async_client.post)(
            self.LIST_URL, data=test_Ad_valid
        )

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.json()
        data_json = json.loads(response_data)
        assert data_json["data"]["id"] > 0
        await close_all(async_client)

    @pytest.mark.ad_create
    @pytest.mark.parametrize(
        "title, expected",
        [
            (["О%бъявление"], status.HTTP_401_UNAUTHORIZED),
            (["О"], status.HTTP_401_UNAUTHORIZED),
        ],
    )
    async def test_title_of_create_ad_invalid(
        self, close_all, async_client, test_Ad_valid, title, expected
    ):
        # Arrrange
        """CREATE AD"""
        test_Ad_valid["title"] = title
        cache.clear()

        # Act
        response = await sync_to_async(async_client.post)(
            self.LIST_URL, data=test_Ad_valid
        )

        # Assert
        logging.info("RESPONSE.STATUS_CODEЖ %s:", str(response))
        assert response.status_code == expected
        await close_all(async_client)
