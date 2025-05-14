"""
ads/models.py
"""

from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUser(AbstractUser):
    """
    This class for storing all the users and customization of users
    """

    username = (models.CharField("username", max_length=150),)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="%(class)s_groups",
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="%(class)s_user_permissions",
        # Уникальное имя для обратной связи
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name="user permissions",
    )


# class Meta:
#     # Add this if you haven't already ','
#     swappable = "AUTH_USER_MODEL"


class Category(models.Model):
    """
    This class is for storing all the categories
    """

    CATEGORY_STATUS = {
        "NEW": _("Новое"),
        "USED": _("Использованное"),
        "UNKNOWN": _("Неизвестно"),
    }

    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class CategoryPath(models.Model):
    """
    This class is for storing the path's templates
    """

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

    def __str__(self):
        return "%s" % (self.path)

    class Meta:
        db_table = "paths"
        verbose_name = _("Path")
        verbose_name_plural = _("Paths")


class Ad(models.Model):
    """
    This class for storing all the ads.
    """

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="author"
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
    status = models.BooleanField(
        default=False,
        help_text=_(
            "Default is False (not activated), if \
you want the public page it means that True"
        ),
        verbose_name=_("Status"),
    )
    category_path = models.ForeignKey(
        CategoryPath,
        on_delete=models.CASCADE,
        related_name="path",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    def __str__(self):
        return "%s, %s" % (self.title, self.category)

    class Meta:
        db_table = "ads"
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")


class ExchangeProposal(models.Model):

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


class MiddleExchange(models.Model):
    """"
    This class for storing the exchange status.\
    "ACCEPTED": This is the status when the buyer accepted offer the seller,\
    "DECLINED": This is the status when the buyer decline the seller offer,
    "WATING": This is the status when the seller or buyer has not made a decision,
    """

    EXCHANGE_STATUS = {
        "ACCEPTED": _("Принял"),
        "DECLINED": _("Отклонен"),
        "WATING": _("Ожидает"),
    }
    status = models.CharField(
        default=EXCHANGE_STATUS.WATING,
        choices=EXCHANGE_STATUS,
        verbose_name=_("Status"),
        help_text=_("Status for the exchange"),
    )
    ad_sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="sender"
    )

    ad_receiver = models.DateField(
        CustomUser, on_delete=models.CASCADE, null=True, related_name="receiver"
    )

    def clean(self):
        if self.ad_sender == self.ad_receiver:
            raise ValueError("ad_sender and ad_receiver cannot be the same")
