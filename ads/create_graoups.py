"""
project/create_graoups.py
"""

"""
project/permitions.py
"""
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from ads.models import Ad


def create_editor_group():
    """GET CONTENT TYPE FOR AD MODEL"""
    content_type = ContentType.objects.get_for_model(Ad)

    """GET OR CREATED THE NEW GROUP"""
    group, create = Group.objects.get_or_create(name="Ad Author")
    """ADD PERMISSIONS FROMM BASIC PERMISSION's SET"""
    permissions = Permission.objects.filter(content_type=content_type, codename__in=[])
    group.permisions.add(*permissions)

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
    group.permissions.add(custom_permissions)


create_editor_group()
