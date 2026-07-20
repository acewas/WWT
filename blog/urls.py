from django.urls import path

from .views import BlogDetailView, BlogListView, CategoryPostListView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("category/<slug:slug>/", CategoryPostListView.as_view(), name="blog_category"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
