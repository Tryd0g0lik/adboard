import asyncio
import logging
import os
import pytest
from playwright.sync_api import Playwright, sync_playwright
from playwright.async_api import Playwright, async_playwright
from project import settings
from django.contrib.auth.models import User
from dotenv import load_dotenv
from logs import configure_logging

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


@pytest.fixture
def check_user_sync(django_db_blocker):
    """Асинхронная версия фикстуры"""
    # yield
    async def check_user_async():
        with django_db_blocker.unblock():
            logging.info("START CHECK OF USER IN DB")

            # Вариант 1: Просто проверка количества пользователей
            # await sync_to_async(User.objects.all().delete)()
            # logging.info(f"Total users in DB: {count}")
#
#             # Вариант 2: Поиск конкретного пользователя
#             user = await sync_to_async(User.objects.filter(username="Sergey").first)()
#             assert user is not None, "User 'Sergey' not found in database"
#             logging.info(f"User found: {user.username}")
#             # logging.info(f"COUNT USER: {count}, {count == 1}")
#             assert count == 1
#             await sync_to_async(user.delete)()

            # counst = await sync_to_async(User.objects.count)()
            # return counst
#         logging.info("END CHECK OF USER IN DB AND CLOSE BROWSER")
    return check_user_async