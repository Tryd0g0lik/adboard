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
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"class": "password"}),
        min_length=3,
        max_length=30,
    )
