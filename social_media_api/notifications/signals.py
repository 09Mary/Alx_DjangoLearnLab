from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from .models import Like
from notifications.models import Notification

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if not created:
        return
    post = instance.post
    actor = instance.user
    recipient = post.author
    if recipient == actor:
        # optionally avoid notifying self-likes
        return
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb='liked',
        target_content_type=ContentType.objects.get_for_model(post),
        target_object_id=post.pk
    )
