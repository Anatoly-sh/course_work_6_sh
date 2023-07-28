from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from users.forms import CastomUserForm
from users.models import User


class ProfileUpdateView(UpdateView):
    model = User
    form_class = CastomUserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):    # переопределение метода для извлечения pk
        return self.request.user

