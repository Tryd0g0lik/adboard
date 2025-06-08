from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.contrib.auth.models import User
from ads.models import Exchange, Ad


@receiver(pre_delete, sender=User)
def project_user_deletion(sender, instance, **kwargs):
    """
    We can delete a user if this user have not an ad and/or there is not\
    different exchanges.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """

    if not transaction.get_autocommit():
        """
        Stop check
        """
        return
    """
    Невозможно удалить пользователя пока есть комментарии которые он отправляет и (или) получает.
    И в комментариях есть изображения принадлежащие пользователю
    """
    if (
        Exchange.objects.filter(ad_sender=instance).exists()
        or Exchange.objects.filter(ad_receiver=instance).exists()
        or Exchange.objects.filter(file_id=instance).exists()
    ):
        raise PermissionDenied(
            _(
                "The exchanges and (or) ads must be delete \
before deletion of this user "
            )
        )
