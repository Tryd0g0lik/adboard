import asyncio
import logging
import os
import pytest
from asgiref.sync import sync_to_async
from playwright.sync_api import sync_playwright, Playwright
from project import settings
from django.contrib.auth.models import User
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(
    autouse=True,
)
async def async_browser(playwright: Playwright):
    """
    This function will be used for launching browser
    :param playwright:
    :return:
    """
    
    logging.info("START BROWSER FIXTURE")
    chromium = await playwright.chromium
    logging.info("RECEIVED CHROMIUM")
    browser = await chromium.launch()
    logging.info("START BROWSER")
    context = await browser.new_context()
    logging.info("START CONTEXT")
    return context

@pytest.fixture(autouse=True)
def django_db_setup():
    settings.DATABASES['default']['TEST'] = {
        'ENGINE': os.getenv("ENGINE"),
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': os.getenv("POSTGRES_HOST"),
        'PORT': os.getenv("POSTGRES_PORT"),
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

# @pytest.fixture(autouse=True)
# async def check_user_async(django_db_blocker):
#     """Асинхронная версия фикстуры"""
#     # yield
#     pass
    # with django_db_blocker.unblock():
    #     logging.info("START CHECK OF USER IN DB")
    #
    #     count = await User.objects.acount()
    #     logging.info(f"COUNT USER: {count}, {count == 1}")
    #     assert count == 1
    #
    #     user = await sync_to_async(User.objects.afilter(username="Sergey").afirst()
    #     assert user is not None
    #     logging.info(f"USER NAME: {user.username}")

#         await user.adelete()
#         logging.info("END CHECK OF USER IN DB AND CLOSE BROWSER")