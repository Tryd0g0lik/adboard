"""
__tests__/playwrigh/test_register_to_the_app.py
"""
import asyncio
import logging
import re
import os
import pytest
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from playwright.sync_api import Page, expect, Playwright
from __tests__.__fixtures__.playwrigth_fixture import async_browser
from logs import configure_logging
load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)

@pytest.mark.asyncio
async def test_register_form_valid(playwright: Playwright):
    log.info("test_register_form_valid")
    chromium = playwright.chromium
    log.info("RECEIVED CHROMIUM")
    browser = await chromium.launch()
    log.info("START BROWSER")
    page = await browser.new_page()
    # page = await browser.new_context()
    log.info("OPEN NEW PAGE")
    result: None
    try:
        await page.goto(f"http://{os.getenv('POSTGRES_HOST')}:8000/users/register/")
        log.info("GOT TO REGISTER PAGE")
        await page.wait_for_load_state("domcontentloaded")
        log.info("PAGE WAS LOADED")
        """CHECK PAGE TITLE"""
        await expect(page).to_have_title(re.compile(r"Регистрация *"))
        # result = await page.locator("title")
        log.info("CHECK THE TITLE OF PAGE")
        """CHECK REGISTER FORM"""
        # page.fill("input[name='username']", "Sergey")
        # page.fill("input[name='email']", "sergey@gmail.com")
        # page.fill("input[name='password']", "123456789")
        # page.fill("input[name='confirm_password']", "123456789")
        await page.wait_for_selector("input[name='username']").fill("Sergey")
        await page.wait_for_selector("input[name='email']").fill("sergey@gmail.com")
        await page.wait_for_selector("input[name='password']").fill("123456789")
        await page.wait_for_selector("input[name='confirm_password']").fill("123456789")
        log.info("INSERT DATA IN REGISTER TORM")
        await page.keyboard.down("Enter")
        log.info("PRESS BY ENTER")
        """CHECK REDIRECT TO LOGIN PAGE"""
        await page.wait_for_load_state("domcontentloaded")
        await expect(page).to_have_title(re.compile(r"Войдите в"))
        log.info("CHECK THE TITLE OF LOGIN PAGE")
        """CHECK OF USER REGISTER IN DB"""
    except Exception as e:
        logging.error("TEST ERROR", e)
    finally:
        
        # Закрываем страницу и браузер
        await page.close()
        log.info("BROWSER CLOSED")


# @pytest.mark.user_page
# def test_register_form_valid(browser):
#     page = browser.new_page()
#     page.goto(f"http://{os.getenv('POSTGRES_HOST')}:8000/users/register/")
#     page.wait_for_load_state('domcontentloaded')
#     """CHECK PAGE TITLE"""
#     expect(page).to_have_title(re.compile(r"Регистрация *"))
#
#     """CHECK REGISTER FORM"""
#     page.wait_for_selector("input[name='username']").fill("Sergey")
#     page.wait_for_selector("input[name='email']").fill("sergey@gmail.com")
#     page.wait_for_selector("input[name='password']").fill("123456789")
#     page.wait_for_selector("input[name='confirm_password']").fill("123456789")
#     page.keyboard.down("Enter")
#     # Wait for the "DOMContentLoaded" event.
#     page.wait_for_load_state("domcontentloaded")
#
#     """CHECK REDIRECT TO LOGIN PAGE"""
#     expect(page).to_have_title(re.compile(r"Войдите в"))

@pytest.mark.user_page
async def main():
    async with async_playwright() as playwright:
        await test_register_form_valid(playwright)


asyncio.run(main())
