from typing import Any, Dict, Optional
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DeleteView
from .models import (
    PostCategory,
    Post
)


# Create your views here.

class BlogLandingPage(TemplateView):
    template_name: str = 'blog/main.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        context['posts'] = Post.objects.filter(status="P").order_by('-created_at')[:10]
        context['landing_page'] = True
        return context


class BlogPostCategory(ListView):
    model = Post
    template_name: str = 'blog/main.html'
    paginate_by: int = 5
    context_object_name: Optional[str] = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categories__slug=self.kwargs['category_slug']).order_by('-created_at')[:5]
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        context['selected_category'] = PostCategory.objects.filter(slug=self.kwargs['category_slug'])[0]
        return context


class BlogPostDetail(DeleteView):
    model = Post
    template_name: str = 'blog/post_details.html'
    context_object_name: Optional[str] = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = PostCategory.objects.all()
        return context