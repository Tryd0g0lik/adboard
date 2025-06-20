import logging
import pytest
import re
from django.contrib.auth.models import User
from playwright.async_api import Playwright
from dotenv import load_dotenv

from ads.models import Ad
from logs import configure_logging

load_dotenv()
log = logging.getLogger(__name__)
configure_logging(logging.INFO)


@pytest.fixture
def cleaning_db(django_db_blocker):
    """Фикстура очистки базы данных"""
    with django_db_blocker.unblock():
        log.info("FIXTURE CLEANING DB")
        User.objects.all().delete()
        log.info("FIXTURE DELETING ALL USERS")
        return True


@pytest.fixture
def delete_one_user(django_db_blocker):
    """Фикстура удаления одного пользователя"""

    def delete_user(username="Sergey"):
        """Функция удаления пользователя"""
        try:
            with django_db_blocker.unblock():
                user = User.objects.filter(username=username).first()
                if not user:
                    return False
                log.info("FIXTURE %s :  GET ONE USER FROM DB" % __name__)
                ads_of_user = Ad.objects.filter(user=user)
                log.info("FIXTURE %s: GOT USER" % __name__)
                log.info("FIXTURE %s: FIRST USER ID: %s" % (__name__, user))

                if not ads_of_user.first():
                    log.info("FIXTURE %s : USER HAS NO ADS" % __name__)
                    user_name = user.username
                    user.delete()
                    log.info("FIXTURE %s : DELETED USER - %s" % (__name__, user_name))
                    return True
                user_name = user.username
                log.info("FIXTURE %s: USER NAME - %s" % (__name__, user_name))
                ads_of_user.delete()
                # [one_ad.delete() for one_ad in list(ads_of_user)]
                log.info(
                    "FIXTURE %s: DELETED ALL ADS OF THIS USER - %s"
                    % (__name__, user_name)
                )
                user.delete()
                log.info("FIXTURE %s : DELETED USER - %s" % (__name__, user_name))
                return True
        except Exception as e:
            log.error("ERROR IN FIXTURE CLEANING DB: %s" % str(e))
            return False

    return delete_user


@pytest.fixture
async def abrowser():

    async def pages(playwright: Playwright):
        log.info("START: %s" % __name__)
        chromium = playwright.chromium
        log.info("RECEIVED CHROMIUM")
        browser = await chromium.launch()
        log.info(" RECEIVED BROWSER")
        context = await browser.new_context()
        log.info("RECEIVED CONTEXT")
        page = await context.new_page()
        log.info("RECEIVED NEW PAGE")
        return page

    return pages


@pytest.fixture
def one_of_ads():

    async def ad_for_one_user(page, url, expect, username):
        """
        This is a simple set of lines/ That will be users registered for testing.
        :param page: this is a page from playwright.
        :param url: this is url 'http://127.0.0.1:8000'
        :param expect:
        :param username: unique username for registration.
        :return: page
        """
        try:
            await page.goto(url + "/users/register/")
            """"REGISTRATION"""
            await page.wait_for_load_state("domcontentloaded")
            log.info(
                "FIXTURE %s: PAGE OF REGISTRATION WAS LOADED" % ad_for_one_user.__name__
            )
            await expect(page).to_have_title(re.compile(r"Регистра"), timeout=3000)
            await page.fill("input[name='username']", username)
            await page.fill("input[name='email']", "ads01@mail.ru")
            await page.fill("input[name='password']", "12345678")
            await page.fill("input[name='confirm_password']", "12345678")
            await page.keyboard.down("Enter")
            await page.wait_for_load_state("domcontentloaded")
            log.info(
                "FIXTURE %s: USER- '%s' REGISTRETED SUCCESSFULLY, WAS"
                % (ad_for_one_user.__name__, username)
            )
            """LOGIN"""
            await page.goto(url + "/users/login/")
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
            log.info(
                "FIXTURE %s: USER - '%s' WAS GOING TO LOGING PAGE"
                % (ad_for_one_user.__name__, username)
            )
            await expect(page).to_have_title(re.compile(r"профиль"))
            await page.fill("input[name='username']", username)
            await page.fill("input[name='password']", "12345678")
            await page.keyboard.down("Enter")
            log.info(
                "FIXTURE %s: USER - '%s' HAS BEEN AUTHORIZED"
                % (ad_for_one_user.__name__, username)
            )
        except Exception as e:
            log.error("FIXTURE %s: ERROR: %s" % (ad_for_one_user.__name__, str(e)))

        finally:
            return page
        # count = await sync_to_async(User.objects.count)()

    return ad_for_one_user
