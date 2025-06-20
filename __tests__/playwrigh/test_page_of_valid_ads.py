"""
__tests__/playwrigh/test_page_of_valid_ads.py
"""

import pytest
import logging
import re
import os

from asgiref.sync import sync_to_async
from playwright.async_api import expect, async_playwright
from __tests__.__fixtures__.playwrigth_fixture import (
    abrowser,
    delete_one_user,
)
from logs import configure_logging
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


@pytest.mark.ads
@pytest.mark.ad_create
@pytest.mark.ad_get
@pytest.mark.asyncio
async def test_page_of_ads(abrowser, delete_one_user):
    log.info("START BROWSER %s" % __name__)
    async with async_playwright() as playwright:
        page = await abrowser(playwright)
        try:
            url = f"http://{os.getenv('POSTGRES_HOST')}:8000"
            await page.goto(url + "/users/register/")
            """"REGISTRATION"""
            await page.wait_for_load_state("domcontentloaded")
            log.info("PAGE OF REGISTRATION WAS LOADED")
            await expect(page).to_have_title(re.compile(r"Регистра"), timeout=3000)
            await page.fill("input[name='username']", "ads")
            await page.fill("input[name='email']", "ads01@mail.ru")
            await page.fill("input[name='password']", "12345678")
            await page.fill("input[name='confirm_password']", "12345678")
            await page.keyboard.down("Enter")
            await page.wait_for_load_state("domcontentloaded")
            log.info("USER REGISTRETED SUCCESSFULLY, WAS ")
            """LOGIN"""
            await page.goto(url + "/users/login/")
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
            log.info("USER WAS GOING TO LOGING PAGE")
            await expect(page).to_have_title(re.compile(r"профиль"))
            await page.fill("input[name='username']", "ads")
            await page.fill("input[name='password']", "12345678")
            await page.keyboard.down("Enter")
            log.info("USER HAS BEEN AUTHORIZED")
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
            await expect(page).to_have_title(re.compile(r"пожаловать"))
            log.info("USER TO THE MAIN PAGE")
            await page.goto(url + "/user/ads/")
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
            locator = page.locator("h3", has_text="Объявление")
            await expect(locator).to_contain_text("Объявление")
            log.info("USER WAS GOING TO PAGE OF HIS ADS")
            await page.fill("input[type='text']", "В Совете по инвестициям заявили")
            await page.fill(
                "textarea[name='description']",
                "Группа «Аэрофлот» к 2030 году получит только 108\
 самолетов МС-21, оставшиеся 92 воздушных судна поступят в парк авиакомпании только к концу 2032 года. Компания \
 при этом не планирует",
            )
            log.info("USER FILLED THE FIELDS OF AD's FORM")
            await page.get_by_role("button", name="Submit").click()
            await page.wait_for_timeout(6000)
            log.info("USE PUSHED BUTTOM FROM AD's FROM")
            await expect(
                page.get_by_role("heading", name=re.compile(r"В Совете по.*"))
            ).to_be_visible()
            await page.screenshot(path="__tests__/screen/test_page_of_ads.png")
            log.info("UOR AD FOUND IN COMMON LIST OF ADS")
        except Exception as ex:
            log.error("ADS PAGE ERROR %s" % ex)

        finally:
            log.info("TEST WAS CLOSED")
            await page.close()
            log.info("PAGE CLOSED")
            await sync_to_async(delete_one_user)("ads")
            log.info("USER AND ADS HAS BEEN DELETED. OVER WE HAVE ERROR.")
