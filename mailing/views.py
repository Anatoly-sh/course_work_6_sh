from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView, UpdateView

from mailing.form import ClientForm, MailSettingForm
from mailing.models import Client, MailSetting, Attempt


class ClientList(ListView):
    model = Client

    def get_queryset(self):
        # queryset = super().get_queryset()
        # if self.request.user.has_perm('main.view_client'):
        #     return queryset
        return Client.objects.filter(author=self.request.user)


class ClientDetail(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user  # запись в таблицу Client автора записи
        return super().form_valid(form)


class ClientUpdate(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self, *args, **kwargs):
        return reverse('mailing:client_detail', args=[self.get_object().pk])


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')
# ---------------------------------------------------------------------------------------


class MailSettingList(ListView):
    model = MailSetting

    def get_queryset(self):
        # queryset = super().get_queryset()
        # if self.request.user.has_perm('main.view_client'):
        #     return queryset
        return MailSetting.objects.filter(author=self.request.user)



class MailSettingDetail(DetailView):
    model = MailSetting


class MailSettingCreate(CreateView):
    model = MailSetting
    form_class = MailSettingForm
    success_url = reverse_lazy('mailing:mail-setting-list')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user  # запись в таблицу Client автора записи
        return super().form_valid(form)


class MailSettingUpdate(UpdateView):
    model = MailSetting
    form_class = MailSettingForm

    def get_success_url(self, *args, **kwargs):
        return reverse('mailing:mail-setting-detail', args=[self.get_object().pk])


class MailSettingDelete(DeleteView):
    model = MailSetting
    success_url = reverse_lazy('mailing:mail-setting-list')
# ---------------------------------------------------------------------------------------


class AttemptView(ListView):
    model = Attempt


class MainPage(TemplateView):
    template_name = 'mailing/base.html'     # временно
