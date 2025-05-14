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
#     # Add this if you haven't already
#     swappable = "AUTH_USER_MODEL"


class Category(models.Model):
    pass

    # NEW = _("Новое"),
    # USED = _("Использованное"),
    class Meta:
        db_table = "categories"
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class CategoryPath(models.Model):
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

    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE,
    #     related_name="categories",
    # )

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        db_table = "ads"
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")


# class ExchangeProposal:
#     ad_sender
