from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "date_subscribed", "is_active")
    list_filter = ("is_active", "date_subscribed")
    search_fields = ("email",)
    list_editable = ("is_active",)
