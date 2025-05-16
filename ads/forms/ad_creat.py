from django import forms
from django.core import validators
from django.utils.translation import gettext_lazy as _

from ads.models import Ad, FileAd

CATEGORY_STATUS = [
    ("NEW", _("Новое")),
    ("USED", _("Использованное")),
    ("UNKNOWN", _("Неизвестно")),
]
PAGE_TEMPLATES = [
    ("SPORT", _("Спорт")),
    ("TECH", _("Техника")),
    ("HOME", _("Дом и сад")),
    ("CLOTHES", _("Одежда и обувь")),
    ("BOOKS", _("Книги")),
    ("CARS", _("Авто")),
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
    )
    files = forms.CharField(
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
    description = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={"class": "form-control ad-full__description is-valid"}
        ),
        help_text="Текст объявления",
    )
    category = forms.CharField(
        widget=forms.Select(
            choices=CATEGORY_STATUS,
            attrs={"class": "form-select"},
        ),
        help_text="Укажите состояние товара",
    )
    path = forms.CharField(
        widget=forms.Select(
            choices=PAGE_TEMPLATES, attrs={"class": "form-select is-valid"}
        ),
        help_text="Укажите категорию товара",
    )

    class Meta:
        model = Ad
        fields = ["title", "description", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for file_name, field in self.fields.items():

            help_text = getattr(
                field,
                "help_text",
            )
            field.help_text = f'<div id=emailHelp"\
class="form-text">{help_text}</div>'

    def clean_image_field(self):
        # images = self.files
        pass
