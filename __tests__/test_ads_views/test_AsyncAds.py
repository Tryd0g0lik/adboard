import json
import pytest
import logging
from model_bakery import baker
from rest_framework import status
from django.core.cache import cache
from asgiref.sync import sync_to_async
from rest_framework.test import APIClient
from ads.models import Ad
from django.db import connections


@pytest.fixture(autouse=True, scope="module")
async def async_client():
    """Create async client"""
    client = await sync_to_async(APIClient)()
    logging.info("ASYNC CLIENT CREATED")
    yield client


@pytest.fixture
def close_all():
    """Close all connection and clients"""

    async def close_all_connections(client):

        await sync_to_async(client.logout)()
        logging.info("ASYNC CLIENT WAS LOGOUT")
        await sync_to_async(connections.close_all)()
        logging.info("CONNECTION WAS ALL CLOSED")

    return close_all_connections


@pytest.fixture
def data_random():
    """Create random data for tests"""

    def factory(*args, **kwargs):
        return baker.make(Ad, *args, **kwargs)

    return factory


@pytest.fixture(autouse=True, scope="function")
def test_Ad_valid(data_random):
    data_ads = data_random(_quantity=10)
    logging.info("DATA RANDOM: %s", data_ads)
    return {
        "title": ["Объявление"],
        "description": ["ОбъявлениеОбъявлениеОбъявлениеОбъявлениеОбъявление"],
        "category": ["UNKNOWN"],
        "condition": ["DEACTIVATED"],
        "path": ["categories/sport/index.html"],
    }


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
class TestAd:
    """Test Ad"""

    LIST_URL = "/api/v1/ads/"

    @pytest.mark.ad_create
    async def test_create_ad_valid(
        self,
        close_all,
        async_client,
        test_Ad_valid,
    ):
        # Arrrange
        """CREATE AD"""

        logging.info("DATA URL: %s", self.LIST_URL)
        logging.info("DATA: %s", test_Ad_valid)
        cache.clear()
        logging.info("CACHE CLEAR")

        # Act
        response = await sync_to_async(async_client.post)(
            self.LIST_URL, data=test_Ad_valid
        )

        logging.info("RESPONSE: %s", response)

        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        logging.info("RESPONSE STATUS CODE: %s", str(response.status_code))
        response_data = response.json()
        logging.info("RESPONSE_DATA TYPE: %s", type(json.loads(response_data)))
        logging.info("RESPONSE_DATA ALL: %s", json.loads(response_data))
        logging.info("RESPONSE_DATA ['DATA']: %s", json.loads(response_data)["data"])
        data_json = json.loads(response_data)
        assert data_json["data"]["id"] > 0
        logging.info("RESPONSE DATA_JSON: %s", data_json)
        await close_all(async_client)

        logging.info("ASYNC CLIENT WAS CLOSED")

    @pytest.mark.ad_create
    @pytest.mark.parametrize(
        "title, expected",
        [
            (["О%бъявление"], status.HTTP_401_UNAUTHORIZED),
            (["О-бъявление"], status.HTTP_401_UNAUTHORIZED),
            (["О"], status.HTTP_401_UNAUTHORIZED),
        ],
    )
    async def test_title_of_create_ad_invalid(
        self, close_all, async_client, test_Ad_valid, title, expected
    ):
        # Arrrange
        """CREATE AD"""
        logging.info("DATA URL: %s", self.LIST_URL)
        logging.info("TITLE DATA: %s", test_Ad_valid["title"])
        test_Ad_valid["title"] = title
        logging.info("TITLE INVALID DATA: %s", test_Ad_valid["title"])
        cache.clear()
        logging.info("CACHE CLEAR")

        # Act
        response = await sync_to_async(async_client.post)(
            self.LIST_URL, data=test_Ad_valid
        )
        logging.info("RESPONSE: %s", response)
        # Assert
        logging.info(
            "RESPONSE STATUS CODE: %s, EXPECTED: %s",
            str(response.status_code),
            str(expected),
        )
        assert response.status_code == expected
        await close_all(async_client)
        logging.info("ASYNC CLIENT WAS CLOSED")


# @pytest.mark.parametrize(
#         "title, description,  condition, path, category, expected", [
#             (['Объявление'],
#              ['ОбъявлениеОбъявлениеОбъявлениеОбъявлениеОбъявление'],
#              ['UNKNOWN'],
#              ['DEACTIVATED'],
#              ['categories/sport/index.html'],
#              status.HTTP_401_UNAUTHORIZED)
#         ]
#     )
