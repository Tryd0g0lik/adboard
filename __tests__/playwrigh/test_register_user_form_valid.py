"""
__tests__/playwrigh/test_register_user_form_valid.py
"""
import logging
import re
import os
import pytest
from dotenv import load_dotenv
from playwright.async_api import async_playwright, Playwright, expect
from __tests__.__fixtures__.playwrigth_fixture import (abrowser, cleaning_db)
from logs import configure_logging

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


# @pytest.mark.django_db(transaction=True)

@pytest.mark.user_page
@pytest.mark.asyncio
async def test_register_form_valid(abrowser, cleaning_db):
    """
    This test check registration user's form with valid data.
    :param abrowser:
    :param cleaning_db:
    :return:
    """
    log.info("START BROWSER %s" % __name__)
    async with async_playwright() as playwright:
        page = await abrowser(playwright)

        try:
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
            
        except (Exception, AssertionError) as e:
            log.info("TEST ERROR", e)
        finally:
            log.info("CONTEXT CLOSED")
            await page.close()
            log.info("PAGE CLOSED")

