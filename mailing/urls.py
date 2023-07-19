from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import ClientList, ClientCreate

app_name = MailingConfig.name


urlpatterns = [
    path('clients/', ClientList.as_view, namespace='clients'),
    path('client_create/', ClientCreate.as_view, namespace='client_create'),

]
