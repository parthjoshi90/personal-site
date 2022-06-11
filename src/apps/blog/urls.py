
from django.urls import path
from .views import BlogLandingPage, BlogPostCategory, BlogPostDetail

app_name = 'blog'

urlpatterns = [
    path('', BlogLandingPage.as_view(), name="blog_home"),
    path('<slug:post_slug>', BlogPostDetail.as_view(), name="post"),
    path('category/<slug:category_slug>', BlogPostCategory.as_view(), name="category_home"),
]