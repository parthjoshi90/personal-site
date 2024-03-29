from django.contrib.sitemaps import Sitemap

from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=Post.PUBLISHED).order_by("-start_publication")

    def lastmod(self, obj):
        return obj.updated_at
