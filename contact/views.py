from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import ContactForm


@require_http_methods(["GET", "POST"])
def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        contact_message = form.save()
        send_mail(
            f"Contact form: {contact_message.subject}",
            contact_message.message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_TO_EMAIL],
            fail_silently=True,
        )
        messages.success(request, "Your message has been sent. We will reply shortly.")
        return redirect("contact")
    return render(request, "contact/contact.html", {"form": form})
