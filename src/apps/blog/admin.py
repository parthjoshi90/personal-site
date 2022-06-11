from django.contrib import admin

# Register your models here.
from .models import PostCategory, Post

class PostCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(PostCategory, PostCategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    # list_display = ("title", "status", "summary", "creation_date", "last_update")
    # list_filter = ("status",)
    # search_fields = ("title", "content")
    # date_hierarchy = "start_publication"
    # fields = ("title", "content", "summary", "status", "start_publication")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
