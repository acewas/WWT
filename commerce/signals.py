from django.db.models.signals import post_save
from django.dispatch import receiver

from newsletter.emails import send_platform_update
from .models import JobOpening, MentorshipCohort, OutreachEvent


@receiver(post_save, sender=JobOpening)
def notify_job_opening(sender, instance, **kwargs):
    if not instance.is_active or not instance.notify_subscribers or instance.notification_sent:
        return
    sent_count = send_platform_update(
        f"New WWT career opportunity: {instance.title}",
        instance.title,
        instance.summary,
        instance.get_absolute_url(),
        "Apply Now",
    )
    if sent_count:
        JobOpening.objects.filter(pk=instance.pk).update(notification_sent=True)


@receiver(post_save, sender=OutreachEvent)
def notify_outreach_event(sender, instance, **kwargs):
    if not instance.is_published or not instance.notify_subscribers or instance.notification_sent:
        return
    sent_count = send_platform_update(
        f"New WWT outreach update: {instance.title}",
        instance.title,
        instance.summary,
        instance.get_absolute_url(),
        "View Outreach",
    )
    if sent_count:
        OutreachEvent.objects.filter(pk=instance.pk).update(notification_sent=True)


@receiver(post_save, sender=MentorshipCohort)
def notify_mentorship_cohort(sender, instance, **kwargs):
    if not instance.is_open or not instance.notify_subscribers or instance.notification_sent:
        return
    sent_count = send_platform_update(
        f"WWT mentorship cohort open: {instance.title}",
        instance.title,
        instance.summary,
        instance.get_absolute_url(),
        "Register",
    )
    if sent_count:
        MentorshipCohort.objects.filter(pk=instance.pk).update(notification_sent=True)
