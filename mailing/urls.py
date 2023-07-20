from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import ClientList, ClientCreate, MainPage, ClientDetailView, ClientDeleteView

app_name = MailingConfig.name


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('client_create/', ClientCreate.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
