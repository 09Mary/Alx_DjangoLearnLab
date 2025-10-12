from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from django.conf import settings
from notifications.models import Notification

User = settings.AUTH_USER_MODEL  # string; for ContentType we need model instance

@receiver(m2m_changed, sender=settings.AUTH_USER_MODEL.__class__)  # not correct; instead handle in view
def following_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
    # NOTE: m2m_changed on self-referential fields is tricky. Instead, create notification explicitly in follow view:
    pass
