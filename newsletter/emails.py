from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string

from .models import Subscriber


def send_subscription_confirmation(subscriber):
    subject = f"Welcome to {settings.SITE_NAME}"
    message = "Thanks for subscribing. You will receive new articles and company updates here."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [subscriber.email], fail_silently=True)


def send_new_post_email(post):
    subscribers = Subscriber.objects.filter(is_active=True)
    sent_count = 0
    for subscriber in subscribers:
        context = {"post": post, "subscriber": subscriber, "site_name": settings.SITE_NAME}
        subject = f"New article: {post.title}"
        text_body = render_to_string("newsletter/new_post_email.txt", context)
        html_body = render_to_string("newsletter/new_post_email.html", context)
        email = EmailMultiAlternatives(subject, text_body, settings.DEFAULT_FROM_EMAIL, [subscriber.email])
        email.attach_alternative(html_body, "text/html")
        if email.send(fail_silently=True):
            sent_count += 1
    return sent_count


def send_platform_update(subject, title, summary, url, label="Read More"):
    subscribers = Subscriber.objects.filter(is_active=True)
    sent_count = 0
    for subscriber in subscribers:
        context = {
            "site_name": settings.SITE_NAME,
            "title": title,
            "summary": summary,
            "url": f"{settings.SITE_URL.rstrip('/')}{url}",
            "label": label,
        }
        text_body = render_to_string("newsletter/platform_update_email.txt", context)
        html_body = render_to_string("newsletter/platform_update_email.html", context)
        email = EmailMultiAlternatives(subject, text_body, settings.DEFAULT_FROM_EMAIL, [subscriber.email])
        email.attach_alternative(html_body, "text/html")
        if email.send(fail_silently=True):
            sent_count += 1
    return sent_count
