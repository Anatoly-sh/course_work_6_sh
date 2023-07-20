from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView

from mailing.form import ClientForm
from mailing.models import Client


class ClientList(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')

    # def form_valid(self, form):
    #     instance = form.save()
    #     instance.author = self.request.user  # запись в таблицу Client автора записи
    #     return super().form_valid(form)


class MainPage(TemplateView):
    template_name = 'mailing/base.html'     # временно
