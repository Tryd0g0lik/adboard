import logging
import pytest
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
                t = ads_of_user.first()
                log.info("FIXTURE %s: FIRST USER ID: %s" % (__name__, t.id))

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
def check_user_sync(django_db_blocker):
    """Асинхронная версия фикстуры"""

    # yield
    async def check_user_async():
        with django_db_blocker.unblock():
            logging.info("START CHECK OF USER IN DB")

            # Вариант 1: Просто проверка количества пользователей
            # await sync_to_async(User.objects.all().delete)()
            # logging.info(f"Total users in DB: {count}")

    #
    #             # Вариант 2: Поиск конкретного пользователя
    #             user = await sync_to_async(User.objects.filter(username="Sergey").first)()
    #             assert user is not None, "User 'Sergey' not found in database"
    #             logging.info(f"User found: {user.username}")
    #             # logging.info(f"COUNT USER: {count}, {count == 1}")
    #             assert count == 1
    #             await sync_to_async(user.delete)()

    # counst = await sync_to_async(User.objects.count)()
    # return counst
    #         logging.info("END CHECK OF USER IN DB AND CLOSE BROWSER")
    return check_user_async
