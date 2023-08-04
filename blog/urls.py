from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogView.as_view(), name='blog-view'),
    # path('clients/', ClientList.as_view(), name='clients'),
]
