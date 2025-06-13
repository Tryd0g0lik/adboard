import asyncio
import logging
import os
import pytest
from asgiref.sync import sync_to_async
from playwright.sync_api import Playwright, sync_playwright
from project import settings
from django.contrib.auth.models import User
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(
    autouse=True,
)
def browser():
    """
    This function will be used for launching browser
    :param playwright:
    :return:
    """
    logging.info("START BROWSER FIXTURE")
    playwright = sync_playwright()
    chromium = playwright.start().chromium
    logging.info("RECEIVED CHROMIUM")
    browser = chromium.launch()
    logging.info("START CONTEXT")
    return browser


@pytest.fixture(autouse=True)
def django_db_setup():
    settings.DATABASES["default"]["TEST"] = {
        "ENGINE": os.getenv("ENGINE"),
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }


#
# @pytest.fixture(autouse=True)
# def check_user(django_db_blocker, django_db_setup):
# def page():
# yield
# with django_db_blocker.unblock():
#     """CHECK OF USER IN DB"""
#     logging.info("START CHECK OF USER IN DB")
#     django_db_blocker.unblock()
#     # django_db_blocker.unblock():
#     logging.info("1")
#
#     count = sync_to_async(User.objects.count())
#     logging.info("COUNT USER", count, count == 1)
#     assert count == 1
#     user = sync_to_async(User.objects.filter(username="Sergey"))
#     assert sync_to_async(user.exists())
#     logging.info("USER NAME", user[0].username)
#     sync_to_async(user[0].delete())
#     sync_to_async(user[0].save())
#     logging.info("END CHECK OF USER IN DB AND CLOSE BROWSER")
#


# def check_user_sync(django_db_blocker):
#     """Асинхронная версия фикстуры"""
#
#     logging.info(f"{__name__}")
#     def check_user_async():
#         with django_db_blocker.unblock():
#             # Удаляем всех пользователей
#             User.objects.all().delete()
#             assert User.objects.count() == 0
#             # logging.info("COUNT USER VALUES: %s"% str(type(count_list)))
#             logging.info(f"GOT LIST OF USERS")
            # count = len(list(count_list))
            # logging.info(f"Total users in DB: {count}")

            # # Вариант 2: Поиск конкретного пользователя
            # user = User.objects.filter(username="Sergey").first()
            # assert user is not None, "User 'Sergey' not found in database"
            # logging.info(f"User found: {user.username}")
            # # logging.info(f"COUNT USER: {count}, {count == 1}")
            # assert count == 1
            # user.delete()
            # user.save()
            # logging.info("END CHECK OF USER IN DB AND CLOSE BROWSER")

    # return check_user_async
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