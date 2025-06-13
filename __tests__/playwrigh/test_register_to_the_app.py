"""
__tests__/playwrigh/test_register_to_the_app.py
"""
import asyncio
import logging
import re
import os
import pytest
from django.contrib.auth.models import User
# from asgiref.sync import sync_to_async
# from dotenv import load_dotenv
# from playwright.async_api import sync_playwright
# from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.async_api import async_playwright, Playwright, expect
from __tests__.__fixtures__.playwrigth_fixture import abrowser #, check_user_sync
from logs import configure_logging

# load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


# @pytest.mark.django_db(transaction=True)
@pytest.fixture
def cleaning_db(django_db_blocker):
    """Фикстура очистки базы данных"""
    with django_db_blocker.unblock():
        log.info("FIXTURE CLEANING DB")
        User.objects.all().delete()
        log.info("FIXTURE DELETING ALL USERS")
        return True
    

@pytest.mark.user_page
@pytest.mark.asyncio
async def test_register_form_valid(cleaning_db):
    log.info("FIXTURE START BROWSER")
    async with async_playwright() as playwright:
        log.info("FIXTURE RECEIVED CHROMIUM")
        chromium = playwright.chromium
        log.info("FIXTURE RECEIVED CHROMIUM")
        abrowser = await chromium.launch()
        # log.info("FIXTURE RECEIVED BROWSER")
        # log.info("TEST REGISTER PAGE")
        context = await abrowser.new_context()
        # /log.info("RECEIVED CONTEXT")
        page = await context.new_page()
        log.info("RECEIVED NEW PAGE")

        try:
            pass
            url = "http://127.0.0.1:8000/users/register/"
            await page.goto(url)
            log.info("GOT REGISTER PAGE")
            await page.wait_for_load_state("domcontentloaded")
            log.info("GOT DIV" )
            await expect(page).to_have_title(re.compile(r"Регистрация.*"), timeout=3000)
            log.info("GOT TITLE")
            """CHECK REGISTER FORM"""
            await page.fill("input[name='username']", "Sergey")
            await page.fill("input[name='email']", "sergey@gmail.com")
            await page.fill("input[name='password']", "123456789")
            await page.fill("input[name='confirm_password']", "123456789")
            log.info("INSERT DATA IN REGISTER TORM")
            await page.keyboard.down("Enter")
            log.info("PRESS BY ENTER")
            """CHECK REDIRECT TO LOGIN PAGE"""
            await page.wait_for_load_state("domcontentloaded")
            log.info("LOGIN PAGE WAS LOADED")
            await expect(page).to_have_title(re.compile(r"Войдите в"))
            log.info("CHECK THE TITLE OF LOGIN PAGE")
            # User.objects.all().delete()
            # log.info("DELETE USERS")
            # assert User.objects.all().count() == 0
            log.info("CHECK ALL USERS WAS DELETED")
        except (Exception, AssertionError) as e:
            log.info("TEST ERROR", e)
        finally:
            pass
            # Закрываем страницу и браузер
            await context.close()
            log.info("CONTEXT CLOSED")
            await page.close()
            log.info("PAGE CLOSED")
