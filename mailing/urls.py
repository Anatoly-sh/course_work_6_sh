from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import ClientList, ClientCreate, MainPage, ClientDetail, ClientDelete, MailSettingList, \
    MailSettingCreate, MailSettingDetail, MailSettingDelete, AttemptView, MailSettingUpdate, ClientUpdate, \
    toggle_activity_mailing

app_name = MailingConfig.name


urlpatterns = [
    path('', cache_page(60)(MainPage.as_view()), name='main'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('client_create/', ClientCreate.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetail.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdate.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDelete.as_view(), name='client_delete'),
    path('mailsetting_list/', MailSettingList.as_view(), name='mail-setting-list'),
    path('mailsetting_create/', MailSettingCreate.as_view(), name='mail-setting-create'),
    path('mailsetting_detail/<int:pk>/', MailSettingDetail.as_view(), name='mail-setting-detail'),
    path('mailsetting_update/<int:pk>/', MailSettingUpdate.as_view(), name='mail-setting-update'),
    path('mailsetting_delete/<int:pk>/', MailSettingDelete.as_view(), name='mail-setting-delete'),
    path('attempt_list/', AttemptView.as_view(), name='attempt-list'),
    path('toggle_mailing/<int:pk>/', toggle_activity_mailing, name='toggle-activity-mailing')
]
