"""
__tests__/playwrigh/test_register_to_the_app.py
"""
import asyncio
import logging
import re
import os
import pytest
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async, async_to_sync
from dotenv import load_dotenv
# from playwright.async_api import sync_playwright
from playwright.sync_api import Playwright, sync_playwright, expect
from __tests__.__fixtures__.playwrigth_fixture import browser, check_user_sync
from logs import configure_logging

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


# @pytest.mark.asyncio


@pytest.mark.user_page
@pytest.mark.django_db(transaction=True)
def test_register_form_valid(browser):
    page = browser.new_page()
    log.info(f"OPEN: {__name__}")
    try:
        page.goto(f"http://{os.getenv('POSTGRES_HOST')}:8000/users/register/")
        log.info("GOT REGISTER PAGE")
        page.wait_for_load_state("domcontentloaded")
        log.info("GOT DIV" )
        expect(page).to_have_title(re.compile(r"Регистрация.*"), timeout=3000)
        log.info("GOT TITLE")
        """CHECK REGISTER FORM"""
        page.fill("input[name='username']", "Sergey")
        page.fill("input[name='email']", "sergey@gmail.com")
        page.fill("input[name='password']", "123456789")
        page.fill("input[name='confirm_password']", "123456789")
        log.info("INSERT DATA IN REGISTER TORM")
        page.keyboard.down("Enter")
        log.info("PRESS BY ENTER")
        """CHECK REDIRECT TO LOGIN PAGE"""
        page.wait_for_load_state("domcontentloaded")
        log.info("LOGIN PAGE WAS LOADED")
        expect(page).to_have_title(re.compile(r"Войдите в"))
        log.info("CHECK THE TITLE OF LOGIN PAGE")
        User.objects.all().delete()
        log.info("DELETE USERS")
        assert User.objects.all().count() == 0
        log.info("CHECK ALL USERS WAS DELETED")
    except (Exception, AssertionError) as e:
        log.error("TEST ERROR", e)
    finally:
        # Закрываем страницу и браузер
        page.close()
        log.info(f"CLOSED: {__name__}")
        
# @pytest.mark.django_db(transaction=True)
# @pytest.mark.asyncio
# async def test_clear_users_with_mark():
#     await sync_to_async(User.objects.all().delete)()
#     assert await sync_to_async(User.objects.count)() == 0
#
# @pytest.mark.user_page
# @pytest.mark.asyncio
# async def test_main(check_user_sync):
#     await test_clear_users_with_mark()
#     # test_register_form_valid()
#     await async_to_sync(check_user_sync)()
#     # asyncio.all_tasks()

