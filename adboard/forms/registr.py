"""
adboard/forms/registr.py
"""
from django import forms
from django.core import validators as valid

from django.utils.translation import gettext_lazy as _


class UserRegister(forms.Form):
    """
    Name and last-name should be at least 3 and less than 30 characters.
    Password should be at least 3 and less than 30 characters.
    Password and repeat password should be the same.
    Email should be valid.
    """

    username = forms.CharField(
        label=_("Your login*"),
        help_text=_("Enter your login"),
        min_length=3,
        max_length=30,
        validators=[
            valid.MinLengthValidator(
                3, message=_("Name should be at least 3 characters")
            ),
            valid.MaxLengthValidator(
                30, _("Name should be less than 30  or 30 characters")
            ),
            valid.RegexValidator(
                regex="(^[a-zA-Z][\wa-zA_Z]+)",
                message=_(
                    "Name should contain only characters\
from a-z and A-Z and digits"
                ),
            ),
        ],
    )

    email = forms.EmailField(
        label=_("Email"),
        max_length=50,
        required=False,
        validators=[
            valid.MaxLengthValidator(50, _("Name should be less than 30 characters")),
            valid.EmailValidator(message=_("Enter valid email")),
        ],
    )
    password = forms.CharField(
        label=_("Password*"),
        widget=forms.PasswordInput(attrs={"class": "password"}),
        min_length=3,
        max_length=30,
        validators=[
            valid.MinLengthValidator(3, _("Password should be at least 3 characters")),
            valid.MaxLengthValidator(
                30,
                _("Password should be less than 30 characters"),
            ),
            valid.RegexValidator(

                regex="([%\w)(}{]+$)",
            ),
        ],
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password*"),
        widget=forms.PasswordInput(attrs={"class": "password confirm_password"}),
        min_length=3,
        max_length=30,
        validators=[
            valid.MinLengthValidator(3, _("Password should be at least 3 characters")),
            valid.MaxLengthValidator(
                30,
                _("Password should be less than 30 characters"),
            ),
            valid.RegexValidator(
                regex="([%\w)(}{]+$)",
            ),
        ],
    )
    