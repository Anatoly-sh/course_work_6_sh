from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from mailing.form import ClientForm
from mailing.models import Client


class ClientList(ListView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy()