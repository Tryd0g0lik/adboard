import pytest
from rest_framework.test import APIClient
from ads.models import Ad


@pytest.fixture
async def client():
    from django.test.client import AsyncClient

    return AsyncClient()


@pytest.fixture
def create_ad():
    def _create_ad(**kwargs):
        return Ad.objects.create(**kwargs)

    return _create_ad


@pytest.fixture
def ad_data():
    # Фикстура с тестовыми данными
    return {
        "title": "Test Ad",
        "description": "Test description",
        "image_url": "http://example.com/image.jpg",
        "condition": "new",
        "category": 1,  # ID существующей категории
    }
