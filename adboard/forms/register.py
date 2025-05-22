"""
adboard/forms/register.py
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
        validators=[
            valid.MinLengthValidator(
                3, message=_("Name should be at least 3 characters")
            ),
            valid.MaxLengthValidator(
                30, _("Name should be less than 30  or 30 characters")
            ),
            valid.RegexValidator(
                regex=r"(^[a-zA-Z][a-zA-Z_]{2,30}$|^$)",
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
            valid.EMPTY_VALUES,
            valid.EmailValidator(message=_("Enter valid email")),
        ],
    )
    password = forms.CharField(
        label=_("Password*"),
        widget=forms.PasswordInput(attrs={"class": "password"}),
        min_length=3,
        max_length=30,
        required=True,
        validators=[
            valid.MinLengthValidator(3, _("Password should be at least 3 characters")),
            valid.MaxLengthValidator(
                30,
                _("Password should be less than 30 characters"),
            ),
            valid.RegexValidator(
                    regex=r"(^[a-zA-Z%0-9}{_%]{2,30}$|^$)",
                message=_("The password's characters is valid"),
            ),
        ],
    )
    confirm_password = forms.CharField(
        label=_("Confirm Password*"),
        widget=forms.PasswordInput(attrs={"class": "password confirm_password"}),
        min_length=3,
        max_length=30,
        required=True,
        validators=[
            valid.MinLengthValidator(3, _("Password should be at least 3 characters")),
            valid.MaxLengthValidator(
                30,
                _("Password should be less than 30 characters"),
            ),
            valid.RegexValidator(
                regex=r"(^[a-zA-Z%0-9}{_%]{2,30}$|^$)",
            ),
        ],
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
