"""
weather/forms/form_register.py
"""

from django import forms
from django.core import validators as valid

from django.utils.translation import gettext_lazy as _


class UserRegisterForm(forms.Form):

    username = forms.CharField(
        label=_("Your login*"),
        help_text=_("Enter your login"),
        min_length=3,
        max_length=30,
        required=True,
    )

    email = forms.EmailField(
        label=_("Email"),
        max_length=50,
        required=False,
        help_text=_("Your@email.com"),
    )
    password = forms.CharField(
        label=_("Password*"),
        widget=forms.PasswordInput(attrs={"class": "password"}),
        min_length=3,
        max_length=30,
        required=True,
        help_text=_("a-zA-Z%0-9{_%"),
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password*"),
        widget=forms.PasswordInput(attrs={"class": "password confirm_password"}),
        min_length=3,
        max_length=30,
        required=True,
        help_text=_("a-zA-Z%0-9{_%"),
    )

    # def __str__(self):
    #     return self.clean_password()
    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     for validator in self.fields["password"].validators:
    #         try:
    #             validator(password)
    #         except Exception as ex:
    #             self.add_error("password", str(ex))
    #     return password
    #
