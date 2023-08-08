from django.conf import settings
from django.core.cache import cache
from django.views.generic import ListView, DetailView

from blog.models import Blog
from mailing.services import get_cached_blog_view


class BlogView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_list'] = get_cached_blog_view()      # НУ кеширование
        return context_data


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_number = obj.views_number + 1
        obj.save()
        return obj
