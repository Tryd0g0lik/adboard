"""
ads/models.py
"""

from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
    MinValueValidator,
)
from django.db import models

# from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    """
    This class for storing all the ads.
    """

    user = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Publisher"),
        help_text=_("This is Index from the publisher of the ad"),
        # validators=[
        #     MinValueValidator(1, message=_("Min value is the 1"))
        # ]
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
    condition = models.BooleanField(
        default=False,
        verbose_name=_("Activated"),
        help_text=_(
            "Default is False (not activated), if you want \
the public page it means that True"
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
    ad_sender = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Sender"),
        help_text=_("This the index of sender"),
        # validators=[
        #     MinValueValidator(1, _("Min value of id is the 1")),
        # ]
    )
    ad_receiver = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Receiver"),
        help_text=_("This the index of receiver"),
        # validators=[
        #     MinValueValidator(1, _("Min value of id is the 1")),
        # ]
    )

    class Meta:
        default_permissions = ["add", "change", "view"]
        db_table = "exchange_proposals"
        verbose_name = _("Exchange Proposal")
        verbose_name_plural = _("Exchange Proposals")

    def clean(self):
        if self.ad_sender == self.ad_receiver:
            raise ValueError("ad_sender and ad_receiver cannot be the same")
