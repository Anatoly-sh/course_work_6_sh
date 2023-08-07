from django.conf import settings
from django.core.cache import cache
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = 'blog_list'
            blog_list = cache.get(key)
            if blog_list is None:
                blog_list = data
                cache.set(key, blog_list)
        else:
            blog_list = data
        return blog_list


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_number = obj.views_number + 1
        obj.save()
        return obj
