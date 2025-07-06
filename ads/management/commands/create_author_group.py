"""
project/create_author_group.py
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from ads.models import Ad


class Command(BaseCommand):
    """
    This script creates command to create the 'Ad Author' group. It's required permissions.
    """

    help = "Creates or updates the 'Ad Author' group with required permissions"

    def handle(self, *args, **options):
        """GET CONTENT TYPE FOR AD MODEL"""
        content_type = ContentType.objects.get_for_model(Ad)

        """GET OR CREATED THE NEW GROUP"""
        ad_author_group, create = Group.objects.get_or_create(name="Ad Author")
        """ADD PERMISSIONS FROMM BASIC PERMISSION's SET"""
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=["add_ad", "change_ad", "delete_ad", "view_ad"],
        )
        ad_author_group.permissions.add(*permissions)

        """ADD CUSTOM PERMISSIONS"""
        custom_permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                "author_can_publish",
                "author_can_edit",
                "author_can_delete",
                "author_can_view",
            ],
        )
        if custom_permissions.exists():
            ad_author_group.permissions.add(*custom_permissions)
        ad_author_group.save()
        print(f"Group '{ad_author_group.name}' created/updated successfully!")
