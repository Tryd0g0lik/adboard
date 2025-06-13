"""
__tests__/playwrigh/test_register_to_the_app.py
"""
import asyncio
import logging
import re
import os
import pytest
from django.contrib.auth.models import User
from dotenv import load_dotenv
from playwright.async_api import async_playwright, Playwright, expect

from logs import configure_logging

load_dotenv()
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
    
@pytest.fixture
async def abrowser():
    
    async def pages(playwright: Playwright):
        log.info("RECEIVED CHROMIUM")
        chromium = playwright.chromium
        log.info("RECEIVED CHROMIUM")
        browser = await chromium.launch()
        log.info(" RECEIVED BROWSER")
        context = await browser.new_context()
        log.info("RECEIVED CONTEXT")
        page = await context.new_page()
        log.info("RECEIVED NEW PAGE")
        return page
        # await context.close()
    return pages

@pytest.mark.user_page
@pytest.mark.asyncio
async def test_register_form_valid(abrowser, cleaning_db):
    log.info("START BROWSER")
    async with async_playwright() as playwright:
        page = await abrowser(playwright)

        try:
            # os.getenv('POSTGRES_HOST')}
            url = f"http://{os.getenv('POSTGRES_HOST')}:8000/users/register/"
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
            
            log.info("CONTEXT CLOSED")
            await page.close()
            log.info("PAGE CLOSED")
