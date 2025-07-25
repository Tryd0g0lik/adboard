# Generated by Django 4.2.17 on 2025-05-21 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0016_alter_ad_options_alter_exchangeproposal_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ad",
            options={
                "permissions": [
                    ("author_can_publish", "Can publish"),
                    ("author_can_edit", "Can edit"),
                    ("author_can_delete", "Can delete"),
                    ("author_can_view", "Can view"),
                ],
                "verbose_name": "Ad",
                "verbose_name_plural": "Ads",
            },
        ),
        migrations.AlterModelOptions(
            name="exchangeproposal",
            options={
                "permissions": [
                    ("author_can_publish", "Can publish"),
                    ("author_can_edit", "Can edit"),
                    ("author_can_delete", "Can delete"),
                    ("author_can_view", "Can view"),
                ],
                "verbose_name": "Exchange Proposal",
                "verbose_name_plural": "Exchange Proposals",
            },
        ),
        migrations.AlterModelOptions(
            name="imagestorage",
            options={
                "permissions": [
                    ("author_can_publish", "Can publish"),
                    ("author_can_delete", "Can delete"),
                    ("author_can_view", "Can view"),
                ],
                "verbose_name": "Path to image",
                "verbose_name_plural": "Paths to images",
            },
        ),
    ]
