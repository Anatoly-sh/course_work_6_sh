from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_number = obj.views_number + 1
        obj.save()
        return obj
