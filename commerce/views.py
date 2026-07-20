from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView

from blog.models import Post
from .forms import JobApplicationForm, MentorshipRegistrationForm
from .models import (
    JobOpening,
    MentorshipCohort,
    OutreachEvent,
    Partner,
    PricingPlan,
    Product,
    Project,
    Service,
    TeamMember,
    Testimonial,
)


class HomeView(TemplateView):
    template_name = "commerce/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active=True)[:3]
        context["products"] = Product.objects.filter(is_active=True, is_featured=True)[:3]
        context["projects"] = Project.objects.filter(is_published=True, is_featured=True)[:3]
        context["jobs"] = JobOpening.objects.filter(is_active=True)[:3]
        context["outreach_events"] = OutreachEvent.objects.filter(is_published=True)[:3]
        context["pricing_plans"] = PricingPlan.objects.all()[:3]
        context["testimonials"] = Testimonial.objects.filter(is_active=True)[:3]
        context["latest_posts"] = Post.objects.published()[:3]
        return context


class AboutView(TemplateView):
    template_name = "commerce/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["team_members"] = TeamMember.objects.filter(is_active=True)
        context["partners"] = Partner.objects.filter(is_active=True)
        return context


class ServicesView(TemplateView):
    template_name = "commerce/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active=True)
        context["pricing_plans"] = PricingPlan.objects.all()
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = "commerce/service_detail.html"
    context_object_name = "service"

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class ProductsView(TemplateView):
    template_name = "commerce/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(is_active=True)
        return context


class ProjectsView(ListView):
    model = Project
    template_name = "commerce/projects.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(is_published=True)


class CareersView(ListView):
    model = JobOpening
    template_name = "commerce/careers.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return JobOpening.objects.filter(is_active=True)


class CareerDetailView(DetailView):
    model = JobOpening
    template_name = "commerce/career_detail.html"
    context_object_name = "job"

    def get_queryset(self):
        return JobOpening.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = kwargs.get("form") or JobApplicationForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = self.object
            application.save()
            messages.success(request, "Your application has been received.")
            return redirect(self.object.get_absolute_url())
        messages.error(request, "Please check the application form.")
        return self.render_to_response(self.get_context_data(form=form))


class OutreachView(ListView):
    model = OutreachEvent
    template_name = "commerce/outreach.html"
    context_object_name = "events"

    def get_queryset(self):
        return OutreachEvent.objects.filter(is_published=True)


class MentorshipView(TemplateView):
    template_name = "commerce/mentorship.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cohorts"] = MentorshipCohort.objects.filter(is_open=True)
        context["form"] = kwargs.get("form") or MentorshipRegistrationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MentorshipRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your mentorship registration has been received.")
            return redirect("mentorship")
        messages.error(request, "Please check the mentorship registration form.")
        return self.render_to_response(self.get_context_data(form=form))


class FAQView(TemplateView):
    template_name = "commerce/faqs.html"
