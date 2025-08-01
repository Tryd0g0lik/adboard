# Generated by Django 4.2.17 on 2025-05-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0004_exchangeproposal_delete_category_delete_categorypath_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="exchangeproposal",
            options={
                "default_permissions": ["add", "change", "view"],
                "verbose_name": "Exchange Proposal",
                "verbose_name_plural": "Exchange Proposals",
            },
        ),
        migrations.RemoveField(
            model_name="ad",
            name="category_path",
        ),
        migrations.RemoveField(
            model_name="ad",
            name="status",
        ),
        migrations.AlterField(
            model_name="exchangeproposal",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACCEPTED", "Принял"),
                    ("DECLINED", "Отклонен"),
                    ("WAITING", "Ожидает"),
                    ("READED", "Прочитано"),
                ],
                default="WAITING",
                help_text="Status for the exchange",
                verbose_name="Status",
            ),
        ),
        migrations.AlterModelTable(
            name="exchangeproposal",
            table="exchange_proposals",
        ),
    ]
