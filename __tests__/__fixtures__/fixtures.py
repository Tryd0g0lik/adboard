import pytest
import logging
from asgiref.sync import sync_to_async
from rest_framework.test import APIClient
from ads.models import Ad
from django.db import connections
from model_bakery import baker


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


@pytest.fixture
def create_ad():
    def _create_ad(**kwargs):
        return Ad.objects.create(**kwargs)

    return _create_ad
