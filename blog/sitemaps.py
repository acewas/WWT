from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return ["home", "about", "services", "products", "contact", "faqs", "blog_list"]

    def location(self, item):
        return reverse(item)
