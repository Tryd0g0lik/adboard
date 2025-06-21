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
    one_of_ads,
)
from logs import configure_logging
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)

valid_ad = {
    "test": "В Совете по инвестициям заявили",
    "description": "Группа «Аэрофлот» к 2030 году получит только 108\
 самолетов МС-21, оставшиеся 92 воздушных судна поступят в парк авиакомпании только к концу 2032 года. Компания \
 при этом не планирует",
}
set_title = set()
set_description = set()


@pytest.mark.ads
@pytest.mark.ad_create
@pytest.mark.ad_get
@pytest.mark.parametrize(
    "user, title, answer",
    [
        (
            "ads_one",
            "1234567890",
            401,
        ),
        (
            "ads_three",
            "1234567890",
            401,
        ),
        (
            "ads_four",
            "К",
            401,
        ),
        (
            "ads_five",
            "Герман Греф назвал активы для вложения ₽1 млн на год и 5 лет;",
            401,
        ),
        (
            "six",
            "",
            401,
        ),
    ],
)
@pytest.mark.asyncio
async def test_title_field_of_ads_invalid(
    abrowser, one_of_ads, delete_one_user, user, title, answer
):
    log.info("START BROWSER %s" % test_title_field_of_ads_invalid.__name__)
    async with async_playwright() as playwright:
        page = await abrowser(playwright)

        try:
            log.info("USER LOGIN '%s' IS STARTING" % user)
            url = f"http://{os.getenv('POSTGRES_HOST')}:8000"
            page = await one_of_ads(page, url, expect, user)
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
            await expect(page).to_have_title(re.compile(r"пожаловать"))
            log.info("USER TO THE MAIN PAGE")
            await page.goto(url + "/user/ads/")
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
            locator = page.locator("h3", has_text="Объявление")
            await expect(locator).to_contain_text("Объявление")
            log.info("USER WAS GOING TO PAGE OF HIS ADS")
            await page.fill("input[type='text']", title)
            await page.fill(
                "textarea[name='description']",
                valid_ad["description"],
            )
            log.info("USER HAS BEEN WRITING FIELDS OF HIS FORM FOR NEW AD")
            await page.get_by_role("button", name="Submit").click()
            await page.screenshot(
                path="__tests__/screen/ads/%s_test_page_of_invalid_ads.png" % user
            )

            log.info(
                "USER HAS BEEN CLICKED ON BUTTON FOR CREATING NEW REQUEST TO SERVER "
            )

            locator = page.locator('p[class="invalid"]')
            log.info("LOCATOR: %s" % locator)
            await expect(locator).to_contain_text(re.compile(r".*valid.*"))

        except Exception as ex:
            log.error("ADS PAGE ERROR %s" % ex)
            set_title.add(user)
        finally:
            log.info("TEST WAS CLOSED")
            await page.close()
            log.info("PAGE CLOSED")
            await sync_to_async(delete_one_user)(user)
            log.info("USER AND ADS HAS BEEN DELETED.")
            log.info("TITLE: HAS BEEN ERROR TO THE NEXT USERS: %s" % set_title)

    @pytest.mark.ads
    @pytest.mark.ad_create
    @pytest.mark.ad_get
    @pytest.mark.parametrize(
        "user, description, answer",
        [
            (
                "ads_one",
                "Сбербанком управляет рыночная конкуренция, которая является залогом успеха любой крупной компании,\
заявил Греф. Он занимает пост председателя правления банка с 2007 года",
                401,
            ),
            (
                "ads_two",
                "Сбербанком управляет рыночная конкуренция, которая является залогом успеха любой крупной компании,\
заявил Греф. Он занимает пост председателя правления банка с 2007 года\
Сбербанком управляет рыночная конкуренция, которая является залогом успеха любой крупной компании,\
заявил Греф. Он занимает пост председателя правления банка с 2007 года\
Сбербанком управляет рыночная конкуренция, которая является залогом успеха любой крупной компании,\
заявил Греф. Он занимает пост председатs",
                401,
            ),
            (
                "ads_three",
                "",
                401,
            ),
            (
                "ads_four",
                "К",
                401,
            ),
            (
                "ads_five",
                "",
                401,
            ),
        ],
    )
    @pytest.mark.asyncio
    async def test_description_field_of_ads_invalid(
        abrowser, one_of_ads, delete_one_user, user, description, answer
    ):
        log.info("START BROWSER: %s" % description.__name__)
        async with async_playwright() as playwright:
            page = await abrowser(playwright)
            try:
                log.info("USER LOGIN '%s' IS STARTING" % user)
                url = f"http://{os.getenv('POSTGRES_HOST')}:8000"
                page = await one_of_ads(page, url, expect, user)
                await page.wait_for_load_state("domcontentloaded", timeout=3000)
                log.info("USER TO THE MAIN PAGE")
                await page.goto(url + "/user/ads/")
                await page.await_for_load_state("domcontentloaded", timeout=3000)
                locator = page.locator("h3", has_text="Объявление")
                await expect(locator).to_contain_text("Объявление")
                log.info("USER WAS GOING TO PAGE OF HIS ADS")
                await page.fill("input[type='text']", valid_ad["title"])
                await page.fill(
                    "textarea[name='description']",
                    description,
                )
                log.info("USER HAS BEEN WRITING FIELDS OF HIS FORM FOR NEW AD")
                await page.get_by_role("button", name="Submit").click()
                await page.screenshot(
                    path="__tests__/screen/ads/%s_test_page_of_invalid_description_ads.png"
                    % user
                )
                log.info(
                    "USER HAS BEEN CLICKED ON BUTTON FOR CREATING NEW REQUEST TO SERVER "
                )
                locator = page.locator('p[class="invalid"]')
                log.info("LOCATOR: %s" % locator)
                await expect(locator).to_contain_text("Value is not valid")

            except Exception as ex:
                log.error("ADS PAGE ERROR %s" % ex)
                set_description.add(user)
            finally:
                log.info("TEST WAS CLOSED")
                await page.close()
                log.info("PAGE CLOSED")
                await sync_to_async(delete_one_user)(user)
                log.info("USER AND ADS HAS BEEN DELETED.")
                log.info(
                    "DESCRIPTION: HAS BEEN ERROR TO THE NEXT USERS: %s"
                    % set_description
                )
