"""
adboard/forms/login.py
"""

from django import forms
from django.core import validators as valid

from django.utils.translation import gettext_lazy as _

class UserLogin(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=50,
        validators=[
            valid.MaxLengthValidator(50, _("Name should be less than 30 characters")),
            valid.EmailValidator(message=_("Enter valid email")),
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
