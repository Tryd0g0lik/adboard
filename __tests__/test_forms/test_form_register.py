import pytest
import logging
from adboard.forms.register import UserRegisterForm


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
        ["Victorovich", "est@test.ru", "ds2Rssa8%sa", "ds2Rssa8%sa", True],
    ]

    """ALL FIELDS valid"""

    @pytest.mark.oll_fields
    @pytest.mark.parametrize(
        "username, email, password, confirm_password, expected", VALID_DATA
    )
    def test_form_valid(self, username, email, password, confirm_password, expected):
        logging.info(
            "form_valid_data USERNAME: %s, EMAILЖ %s, PASSWORD: %s, CONFIRM_PASSWORD: %s, EXPECTED: %s",
            username,
            email,
            password,
            confirm_password,
            expected,
        )
        form = UserRegisterForm(
            data={
                "username": username,
                "email": email,
                "password": password,
                "confirm_password": confirm_password,
            }
        )
        logging.info("form_data: %s", form.data)
        assert form.is_valid() == expected

    """PASSWORD"""

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "password, expected",
        [
            ["ds_2Rssa8%sa", True],
            ["ds2%Rssa8%sa", True],
        ],
    )
    def test_PASSWORD_valid(self, valid_form_data_fixture, password, expected):
        form_data = valid_form_data_fixture
        logging.info("form_valid_data: %s", form_data[0])
        form_data[0]["password"] = password
        form_data[0]["confirm_password"] = password
        form = UserRegisterForm(data=form_data[0])
        logging.info("form_data: %s", form.data)
        assert form.is_valid() == expected

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "password, expected",
        [
            ["ds 2Rssa8% sa", False],
            [" ds2%Rssa8%-sa", False],
            ["d-s2%Rssa8%-sa", False],
            ["2ds2%Rssa8%-sa", False],
        ],
    )
    def test_PASSWORD_invalid(self, valid_form_data_fixture, password, expected):
        form_data = valid_form_data_fixture
        logging.info("form_valid_data: %s", form_data[0])
        form_data[0]["password"] = password
        form_data[0]["confirm_password"] = password
        form = UserRegisterForm(data=form_data[0])
        assert form.is_valid() == expected

    """USERNAME"""

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "username, expected",
        [
            ["te d", False],
            ["test user", False],
            ["", False],
            ["%-_", False],
        ],
    )
    def test_USERNAME_invalid(self, valid_form_data_fixture, username, expected):
        form_data = valid_form_data_fixture[0]
        form_data["username"] = username
        logging.info("USERNAME: %s", username)
        logging.info("form_invalid_data: %s, Expect: %s", form_data, expected)
        form = UserRegisterForm(data=form_data)
        assert form.is_valid() == expected

    @pytest.mark.form_register
    @pytest.mark.parametrize("expected", [True])
    def test_USERNAME_valid(self, valid_form_data_fixture, expected):
        form = UserRegisterForm(data=valid_form_data_fixture[0])
        logging.info("form_invalid_data: %s, Expect: %s", form, expected)
        assert form.is_valid() == expected

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "email, expected",
        [
            ["test@test.com", True],
            ["te0st@test.ru", True],
            ["test_01@test.com", True],
            ["0test@test.com", True],
        ],
    )
    def test_EMAIL_valid(self, valid_form_data_fixture, email, expected):
        form_data = valid_form_data_fixture
        form_data[0]["email"] = email
        form = UserRegisterForm(data=form_data[0])
        assert form.is_valid() == expected

    @pytest.mark.form_register
    @pytest.mark.parametrize(
        "email, expected",
        [
            ["testtest.com", False],
            ["te0st@testru", False],
            ["test_01@test.", False],
        ],
    )
    def test_EMAIL_invalid(self, valid_form_data_fixture, email, expected):
        form_data = valid_form_data_fixture
        form_data[0]["email"] = email
        form = UserRegisterForm(data=form_data[0])
        assert form.is_valid() == expected
