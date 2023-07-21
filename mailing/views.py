from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView

from mailing.form import ClientForm, MailSettingForm
from mailing.models import Client, MailSetting


class ClientList(ListView):
    model = Client


class ClientDetail(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')

    # def form_valid(self, form):
    #     instance = form.save()
    #     instance.author = self.request.user  # запись в таблицу Client автора записи
    #     return super().form_valid(form)


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')
# ---------------------------------------------------------------------------------------


class MailSettingList(ListView):
    model = MailSetting


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


class MailSettingDelete(DeleteView):
    model = MailSetting
    success_url = reverse_lazy('mailing:mail-setting-list')
# ---------------------------------------------------------------------------------------


class MainPage(TemplateView):
    template_name = 'mailing/base.html'     # временно
