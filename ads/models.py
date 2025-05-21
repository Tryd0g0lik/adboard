"""
ads/models.py
"""

import datetime

from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
    MinValueValidator,
)
from django.db import models, transaction

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    """
    This class for storing all the ads.
    """

    # Не возможно удалить пользователя пока не удалим его объявления и прочее.
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Sender"),
        help_text=_("This the index of sender"),
        related_name="author",
    )
    title = models.CharField(
        max_length=100,
        unique=True,
        help_text=_(
            "The title is unique and must have a length \
before 100 symbols.\n Min length is the 3 symbols."
        ),
        verbose_name="Title",
        validators=[
            MaxLengthValidator(
                limit_value=100, message=_("Max length (of title) 100 symbols")
            ),
            MinLengthValidator(
                limit_value=3, message=_("Min length (of title) 3 symbols")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-zA-Zа-яА-ЯёЁ][\w \-_\dа-яА-ЯёЁ]{1,48}[a-zA-Zа-яА-ЯёЁ]$[^\S\W \\]?",
                message=_("The title not have correct format."),
            ),
        ],
    )
    description = models.TextField(
        max_length=500,
        validators=[
            MinLengthValidator(
                limit_value=10, message=_("Min length is the 10 symbols")
            ),
            MaxLengthValidator(limit_value=50, message=_("Max length 500 symbols")),
        ],
        help_text=_("Description for the ad"),
        verbose_name=_("Description"),
    )
    image_url = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        help_text=_("The path to the image"),
        validators=[
            MaxLengthValidator(
                limit_value=100, message=_("Max length (of path) 100 symbols")
            ),
            MinLengthValidator(
                limit_value=1, message=_("Min length (of path) 1 symbols")
            ),
            RegexValidator(
                regex=r"(\/||^(?!.*  )[a-z][\w\-_\d]{1,9}\/$[^\S\W ])",
                message=_("The path has the invalid format"),
            ),
        ],
        verbose_name="path",
    )
    created_at = models.DateField(
        auto_now_add=True,
        help_text=_("Date when the ad was created"),
        editable=False,
        verbose_name=_("Created at"),
    )
    STATE = [("ACTIVATED", _("Опубликовано")), ("DEACTIVATED", _("Не опубликовано"))]
    condition = models.CharField(
        default="Не опубликовано",
        choices=STATE,
        verbose_name=_("Activated"),
        help_text=_(
            "By default is state 'Не опубликовано, if you want to public \
your ad choose  'Опубликовано'. This means what your ad wil be public."
        ),
    )
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
    path = models.CharField(
        default=TECH,
        choices=PAGE_TEMPLATES,
        verbose_name=_("Here is the choose category for publication."),
    )
    # category_path = models.CharField(
    #     default=str(PAGE_TEMPLATES[3]),
    #     choices=PAGE_TEMPLATES,
    #     help_text="pathname",
    # )
    CATEGORY_STATUS = [
        ("NEW", _("Новое")),
        ("USED", _("Использованное")),
        ("UNKNOWN", _("Неизвестно")),
    ]
    category = models.CharField(default="UNKNOWN", choices=CATEGORY_STATUS)

    def __str__(self):
        return "%s, %s" % (self.title, self.category)

    class Meta:
        db_table = "ads"
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")
        permissions = [
            ("author_can_publish", _("Can publish")),
            ("author_can_edit", _("Can edit")),
            ("author_can_delete", _("Can delete")),
            ("author_can_view", _("Can view")),
        ]

    def delete(self, using=None, keep_parents=False):
        with transaction.atomic():
            # The every one of ads removing
            ExchangeProposal.objects.filter(exchange__ad_id=self).delete()
            # The every one of exchange proposals removing
            Exchange.objects.filter(ad_id=self).delete()
            # Delete the Image's collection
            object_list = FileAd.objects.filter(ad_id=self)
            for file in object_list:
                file.delete()
            super().delete(using, keep_parents)


class ExchangeProposal(models.Model):
    """
    This class for storing all the exchange proposals

    "ACCEPTED": This is the status when the buyer accepted offer the seller,\
    "DECLINED": This is the status when the buyer decline the seller offer,\
    "WATING": This is the status when the seller or buyer has \
    not made a decision,
    """

    comment = models.TextField(
        help_text=_("Text of the comment. Min. 150 and Max. 1200. "),
        verbose_name=_("Comment"),
        max_length=1200,
        validators=[
            MinLengthValidator(150, _("Min length of comment is the 150 symbols")),
            MaxLengthValidator(1200, _("Max length of comment is the 1200 symbols")),
            RegexValidator(
                regex=r"^(?!.*  )[a-zA-Zа-яА-ЯёЁ][\w \-_\dа-яА-ЯёЁ]{1,}[^\S\W \\]?",
                message=_("The text not have correct format."),
            ),
        ],
    )
    created_at = models.DateField(
        auto_now_add=True,
        help_text=_("Date when the comment was created"),
    )

    class Meta:
        # default_permissions = ["add", "change", "view"]
        db_table = "exchange_proposals"
        verbose_name = _("Exchange Proposal")
        verbose_name_plural = _("Exchange Proposals")
        permissions = [
            ("author_can_publish", _("Can publish")),
            ("author_can_edit", _("Can edit")),
            ("author_can_delete", _("Can delete")),
            ("author_can_view", _("Can view")),
        ]


class Exchange(models.Model):
    EXCHANGE_STATUS = [
        ("ACCEPTED", _("Принял")),
        ("DECLINED", _("Отклонен")),
        ("WAITING", _("Ожидает")),
        ("READED", _("Прочитано")),
    ]

    status = models.CharField(
        default="WAITING",
        choices=EXCHANGE_STATUS,
        verbose_name=_("Status"),
        help_text=_("Status for the exchange"),
    )
    # Объявление не можем про-так удалить пока есть комментария.
    ad_id = models.ForeignKey(
        Ad,
        on_delete=models.PROTECT,
        related_name="ad",
    )
    # Разрешаем удаление комментария
    comment_id = models.ForeignKey(
        ExchangeProposal,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Proposal"),
        help_text=_("This the index of comment (Exchange proposal)"),
        related_name="comment_id",
    )
    # Запрещаем удаление User
    ad_sender = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=_("Sender"),
        help_text=_("This the index of sender"),
        related_name="ad_sender",
        # validators=[
        #     MinValueValidator(1, _("Min value of id is the 1")),
        # ]
    )

    # Пользователя не можем про-так удалить, пока есть объявления и комментарии.
    ad_receiver = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=_("Receiver"),
        help_text=_("This the index of receiver"),
        related_name="ad_receiver",
        # validators=[
        #     MinValueValidator(1, _("Min value of id is the 1")),
        # ]
    )
    file_id = models.ForeignKey(
        "ImageStorage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Image upload path"),
    )

    class Meta:
        # default_permissions = ["add", "change", "view"]

        verbose_name = _("Exchange")
        verbose_name_plural = _("Exchanges")

    def clean(self):
        if self.ad_sender == self.ad_receiver:
            raise ValueError("ad_sender and ad_receiver cannot be the same")


def receive_image_path(instance, filename):
    """ "
    Path to image files.
    """
    list_of_date = str(datetime.date.today()).split("-")
    path = (
        "uploads/" + "999".zfill(4) + "/"
        if instance.user is None
        else str(instance.user.pk) + "/"
    )
    path += "/{}/{}/{}/".format(list_of_date[0], list_of_date[1], list_of_date[2])
    return f"{path}/images/{filename}"


class ImageStorage(models.Model):
    """ "
    File upload path model
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # original_name = models.CharField(_("File name"), max_length=100)
    size = models.PositiveIntegerField(
        _("File weight"),
    )
    upload_date = models.DateField(
        _("Date upload"),
        editable=False,
        auto_now_add=True,
    )
    file_path = models.FileField(
        upload_to=receive_image_path,
        verbose_name=_("Image"),
        help_text=_(
            "Upload image/files. Pathname has a template format is: 'media/<user_pk>/%Y/%m/%d/' "
        ),
    )

    class Meta:
        db_table = "image_storage"
        verbose_name = _("Path to image")
        verbose_name_plural = _("Paths to images")
        permissions = [
            ("author_can_publish", _("Can publish")),
            ("author_can_delete", _("Can delete")),
            ("author_can_view", _("Can view")),
        ]

    def __str__(self):
        return self.file_path


class FileAd(models.Model):
    file_id = models.ForeignKey(
        ImageStorage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Image upload path"),
    )
    ad_id = models.ForeignKey(
        Ad,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
