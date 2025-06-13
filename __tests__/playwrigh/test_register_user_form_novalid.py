import logging
import os
import re
import pytest
from django.core.cache import cache
from dotenv import load_dotenv
from playwright.async_api import (async_playwright, Playwright, expect)

from __tests__.__fixtures__.playwrigth_fixture import (abrowser, cleaning_db)
from logs import configure_logging

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)

valid_data = {'name': 'Elena', 'email': 'elena09@gmail.com',
              'password': 'qwerty12345', 'confirm_password': 'qwerty12345'}

@pytest.mark.user_page
@pytest.mark.user_page_invalid
@pytest.mark.parametrize(
    "username, expected",
    [
        ("", 1),
        # ("1234567890123456789001234567890", "The maximum length of the username is 15 characters"),
    ]
    )
@pytest.mark.asyncio
async def test_filed_username_invalid(abrowser, cleaning_db, username, expected):
    """
    This is the test function for registering a user with invalid data
    :param page:
    :param playwright:
    :return:
    """
    valid_data['name'] = username
    cache.clear()
    log.info("START BROWSER %s" % __name__)
    async with async_playwright() as playwright:
        log.info("GOT PLAYWRIGHT")
        page = await abrowser(playwright)
        log.info("GOT PAGE")
        try:
            url = f"http://{os.getenv('POSTGRES_HOST')}:8000/users/register/"
            await page.goto(url)
            log.info("GOT REGISTER PAGE")
            await page.wait_for_load_state("domcontentloaded")
            log.info("PAGE WAS LOADED")
            await expect(page).to_have_title(re.compile(r"Регистрация.*"), timeout=3000)
            log.info("GOT TITLE")
            """CHECK REGISTER FORM"""
            await page.fill("input[name='username']", str(valid_data["name"]))
            await page.fill("input[name='email']", str(valid_data["email"]))
            await page.fill("input[name='password']", str(valid_data["password"]))
            await page.fill("input[name='confirm_password']", str(valid_data["confirm_password"]))
            log.info("FILLED FIELDS IN REGISTER FORM")
            await page.keyboard.down("Enter")
            log.info("PRESSED ENTER")
            await page.screenshot(path="__tests__/screen/register_user_form_invalid.png")
            log.info("RECEIVED SCREENSHOT OF PAGE")
            locator = page.locator("p[class='invalid']")
            log.info("GOT CURRENT QUANTITY OF ERROR")
            await expect(locator).to_have_count(expected)
            log.info("OK - CHECKED QUANTITY OF ERROR")
        except Exception as e:
            log.info("NOT OK")
            log.info("TEST ERROR", e)
        finally:
            log.info("CONTEXT CLOSED")
            await page.close()
            log.info("PAGE CLOSED")

