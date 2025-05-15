from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from ads.models import Exchange, Ad


@receiver(pre_delete, sender=Ad)
def project_ad_deletion(sender, instance, **kwargs):
    """ "
    Delete the ad if not the exchange
    """
    if not transaction.get_autocommit():
        """
        Stop checking.
        """
        return

    if (
        Exchange.objects.filter(ad_id=instance).exists()
        or Exchange.objects.filter(ad_id=instance).exists()
    ):
        raise PermissionDenied(_("Cannot delete this ad if have exists an exchanges"))
