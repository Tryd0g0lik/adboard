import pytest
import logging
from django.core.cache import cache
from adboard.forms.register import UserRegisterForm
from __tests__.__fixtures__.fixtures import (
    test_Ad_valid,
    data_random,
    async_client,
    close_all,
)
from logs import configure_logging

log = logging.getLogger(__name__)
configure_logging(logging.INFO)



@pytest.fixture
def valid_form_data_fixture():
    return (
        {
            "username": "Victorovich",
            "email": "est@test.ru",
            "password": "ds2Rssa8%sa",
            "confirm_password": "ds2Rssa8%sa",
        },
    )


class TestRegistrationForm:
    VALID_DATA = [
        ["Victorovich", "est@test.ru", "ds2Rssa8%sa", "ds2Rssa8%sa"],
    ]

    """ALL FIELDS valid"""

    @pytest.mark.oll_fields
    @pytest.mark.parametrize("username, email, password, confirm_password", VALID_DATA)
    def test_form_valid(self, username, email, password, confirm_password):
        form = UserRegisterForm(
            data={
                "username": username,
                "email": email,
                "password": password,
                "confirm_password": confirm_password,
            }
        )
        logging.info("form_data: %s", form.data)
        assert form.is_valid()

    """PASSWORD"""

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "password",
        [
            "ds_2Rssa8%sa",
            "ds2%Rssa8%sa",
        ],
    )
    def test_PASSWORD_valid(self, valid_form_data_fixture, password):
        form_data = valid_form_data_fixture
        logging.info("form_valid_data: %s", form_data[0])
        form_data[0]["password"] = password
        form_data[0]["confirm_password"] = password
        form = UserRegisterForm(data=form_data[0])
        logging.info("form_data: %s", form.data)
        assert form.is_valid()

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "password",
        [
            "ds 2Rssa8% sa",
            " ds2%Rssa8%-sa",
            "d-s2%Rssa8%-sa",
            "2ds2%Rssa8%-sa",
        ],
    )
    def test_PASSWORD_invalid(self, valid_form_data_fixture, password):
        form_data = valid_form_data_fixture
        logging.info("form_valid_data: %s", form_data[0])
        form_data[0]["password"] = password
        form_data[0]["confirm_password"] = password
        form = UserRegisterForm(data=form_data[0])
        assert not form.is_valid()

    """USERNAME"""

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "username",
        [
            "te d",
            "test user",
            "",
            "%-_",
        ],
    )
    def test_USERNAME_invalid(self, valid_form_data_fixture, username):
        form_data = valid_form_data_fixture[0]
        form_data["username"] = username
        logging.info("USERNAME: %s", username)
        logging.info("form_invalid_data: %s", form_data)
        form = UserRegisterForm(data=form_data)
        assert not form.is_valid()

    @pytest.mark.form_register
    def test_USERNAME_valid(self, valid_form_data_fixture):
        form = UserRegisterForm(data=valid_form_data_fixture[0])
        logging.info("form_invalid_data: %s", form)
        assert form.is_valid()

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "email",
        [
            "test@test.com",
            "te0st@test.ru",
            "test_01@test.com",
            "0test@test.com",
        ],
    )
    def test_EMAIL_valid(self, valid_form_data_fixture, email):
        form_data = valid_form_data_fixture
        form_data[0]["email"] = email
        form = UserRegisterForm(data=form_data[0])
        assert form.is_valid()

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "email",
        [
            "testtest.com",
            "te0st@testru",
            "test_01@test.",
        ],
    )
    def test_EMAIL_invalid(self, valid_form_data_fixture, email):
        form_data = valid_form_data_fixture
        form_data[0]["email"] = email
        form = UserRegisterForm(data=form_data[0])
        assert not form.is_valid()
