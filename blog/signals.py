from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from newsletter.emails import send_new_post_email
from .models import Post


@receiver(post_save, sender=Post)
def notify_subscribers_on_publish(sender, instance, created, **kwargs):
    if not instance.published or instance.newsletter_sent or instance.published_at > timezone.now():
        return
    sent_count = send_new_post_email(instance)
    if sent_count:
        Post.objects.filter(pk=instance.pk).update(newsletter_sent=True)
