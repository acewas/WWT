from django.contrib import admin

from .models import (
    JobApplication,
    JobOpening,
    MentorshipCohort,
    MentorshipRegistration,
    OutreachEvent,
    Partner,
    PricingPlan,
    Product,
    Project,
    Service,
    TeamMember,
    Testimonial,
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "area", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("area", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_featured", "is_active")
    list_editable = ("is_featured", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active")
    list_editable = ("is_active",)
    search_fields = ("name", "quote", "role")


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "order", "is_featured")
    list_editable = ("order", "is_featured")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "role", "bio")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "website", "is_active")
    list_editable = ("is_active",)
    search_fields = ("name", "description")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "project_type", "year", "is_featured", "is_published")
    list_filter = ("project_type", "is_featured", "is_published", "year")
    list_editable = ("is_featured", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description", "client", "location")


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "employment_type", "is_active", "closing_date", "notification_sent")
    list_filter = ("employment_type", "is_active", "closing_date")
    list_editable = ("is_active",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "requirements")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "job", "email", "created_at", "reviewed")
    list_filter = ("reviewed", "created_at", "job")
    list_editable = ("reviewed",)
    search_fields = ("full_name", "email", "cover_letter")
    readonly_fields = ("created_at",)


@admin.register(OutreachEvent)
class OutreachEventAdmin(admin.ModelAdmin):
    list_display = ("title", "program_type", "location", "event_date", "is_published", "notification_sent")
    list_filter = ("program_type", "is_published", "event_date")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description", "location")


@admin.register(MentorshipCohort)
class MentorshipCohortAdmin(admin.ModelAdmin):
    list_display = ("title", "track", "start_date", "application_deadline", "is_open", "notification_sent")
    list_filter = ("track", "is_open", "start_date")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description")


@admin.register(MentorshipRegistration)
class MentorshipRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "cohort", "email", "university_or_organization", "created_at", "reviewed")
    list_filter = ("reviewed", "created_at", "cohort")
    list_editable = ("reviewed",)
    search_fields = ("name", "email", "university_or_organization", "interests", "goals")
    readonly_fields = ("created_at",)
