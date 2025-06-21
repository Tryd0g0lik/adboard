from django import forms
from django.core import validators
from django.utils.translation import gettext_lazy as _

from ads.models import Ad, FileAd

CATEGORY_STATUS = [
    ("UNKNOWN", _("Неизвестно")),
    ("NEW", _("Новое")),
    ("USED", _("Использованное")),
]
# This is the basis templates of category
SPORT = "categories/sport/index.html"
TECH = "categories/tech/index.html"
HOME = "categories/home/index.html"
CLOTHES = "categories/clothes/index.html"
BOOKS = "categories/books/index.html"
CARS = "categories/cars/index.html"

PAGE_TEMPLATES = [
    (SPORT, _("Спорт")),
    (TECH, _("Техника")),
    (HOME, _("Дом и сад")),
    (CLOTHES, _("Одежда и обувь")),
    (BOOKS, _("Книги")),
    (CARS, _("Авто")),
]
STATE = [
    ("DEACTIVATED", _("Не опубликовано")),
    ("ACTIVATED", _("Опубликовано")),
]


class adCreatForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the title is-valid",
                "id": "validationServer01",
            }
        ),
        help_text=_("before 100 symbols: 'a-zA-Z_0-9'"),
    )

    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={"class": "form-control ad-full__description is-valid"}
        ),
        help_text=_("Content of ad. Max length 500 symbols: 'a-zA-Z_0-9!.?'"),
    )
    category = forms.CharField(
        widget=forms.Select(
            choices=CATEGORY_STATUS,
            attrs={"class": "form-select"},
        ),
        help_text=_("Please, specify the category of the product."),
    )
    condition = forms.CharField(
        widget=forms.Select(choices=STATE, attrs={"class": "form-select"}),
        help_text=_("Please, specify the condition of the ad (publication or not)."),
    )
    path = forms.CharField(
        widget=forms.Select(
            choices=PAGE_TEMPLATES, attrs={"class": "form-select is-valid"}
        ),
        help_text=_("Please, specify the category of the product."),
    )

    class Meta:
        model = Ad
        fields = ["title", "description", "category"]


class FileImageForm(forms.ModelForm):
    class Meta:
        model = FileAd
        fields = "__all__"

    file_path = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control", "id": "validationServer02"}
        ),
        help_text="Формат: 'jpg', 'jpeg', 'png'",
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png"]
            ),
        ],
    )
