"""
adboard/forms/login.py
"""

from django import forms
from django.core import validators as valid

from django.utils.translation import gettext_lazy as _


class UserLogin(forms.Form):
    username = forms.CharField(
        label=_("login"),
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
    password = forms.CharField(
        label=_("Password"),
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
                regex="([\w%)(}{]+$)",
            ),
        ],
    )
