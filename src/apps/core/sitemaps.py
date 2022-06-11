from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ["home", "about", "blog:posts"]

    def location(self, item):
        return reverse(item)
