from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .emails import send_subscription_confirmation
from .forms import SubscriberForm
from .models import Subscriber


@require_POST
def subscribe(request):
    form = SubscriberForm(request.POST)
    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "home"
    if not form.is_valid():
        messages.error(request, "Please enter a valid email address.")
        return redirect(next_url)

    email = form.cleaned_data["email"]
    subscriber, created = Subscriber.objects.get_or_create(email=email, defaults={"is_active": True})
    if not created and not subscriber.is_active:
        subscriber.is_active = True
        subscriber.save(update_fields=["is_active"])

    if created:
        send_subscription_confirmation(subscriber)
        messages.success(request, "You are subscribed. Please check your inbox for confirmation.")
    else:
        messages.info(request, "That email is already subscribed.")
    return redirect(next_url)
