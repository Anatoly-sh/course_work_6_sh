from django.contrib import admin
from django.urls import path, include

from mailing.apps import MailingConfig
from mailing.views import ClientList, ClientCreate, MainPage, ClientDetail, ClientDelete

app_name = MailingConfig.name


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('client_create/', ClientCreate.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetail.as_view(), name='client_detail'),
    path('client_delete/<int:pk>/', ClientDelete.as_view(), name='client_delete'),
    path('mailsetting_list/', MailSettingList.as_view(), name='mail-setting-list'),
    # path('mailsetting_create/', MailSettingCreate.as_view(), name='mail-setting-create'),
    # path('mailsetting_detail/<int:pk>/', mailsettingDetailView.as_view(), name='mail-setting-detail'),
    # path('mailsetting_delete/<int:pk>/', mailsettingDeleteView.as_view(), name='mail-setting-delete'),
]
