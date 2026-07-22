from django.urls import path

from .views import (
    AboutView,
    CareerDetailView,
    CareersView,
    FAQView,
    HomeView,
    MentorshipView,
    OutreachView,
    ProductsView,
    ProjectsView,
    ServiceDetailView,
    ServicesView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("services/", ServicesView.as_view(), name="services"),
    path("services/<slug:slug>/", ServiceDetailView.as_view(), name="service_detail"),
    path("products/", ProductsView.as_view(), name="products"),
    path("projects/", ProjectsView.as_view(), name="projects"),
    path("careers/", CareersView.as_view(), name="careers"),
    path("careers/<slug:slug>/", CareerDetailView.as_view(), name="career_detail"),
    path("outreach/", OutreachView.as_view(), name="outreach"),
    path("mentorship/", MentorshipView.as_view(), name="mentorship"),
    path("faqs/", FAQView.as_view(), name="faqs"),
]
