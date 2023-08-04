from django.views.generic import ListView

from blog.models import Blog


class BlogView(ListView):
    model = Blog
