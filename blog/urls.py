from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView, BlogDetailView

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogView.as_view(), name='blog-view'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail-view'),
    # path('clients/', ClientList.as_view(), name='clients'),
]
