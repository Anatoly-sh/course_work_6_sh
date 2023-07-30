from django.contrib.auth.forms import UserChangeForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django_email_verification import send_email

from config import settings
from users.forms import CastomUserForm, CastomUserRegisterForm
from users.models import User


class ProfileUpdateView(UpdateView):
    model = User
    form_class = CastomUserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):  # переопределение метода для извлечения pk: он не нужен,
        # тк редактируется текущий пользователь
        return self.request.user


class RegisterView(CreateView):
    """
    https://thecodingprocess.hashnode.dev/creating-a-registration-form-with-email-verification-in-django
    https://github.com/LeoneBacciu/django-email-verification
    """
    model = User
    form_class = CastomUserRegisterForm
    success_url = reverse_lazy('users:profile')

    # def form_valid(self, form):  # переопределяем для отправки письма-приветствия о регистрации
    #     register_user = form.save()
    #     send_mail(
    #         subject='Поздравляем с регистрацией',
    #         message='Вы зарегистрировались на платформе рассылок, добро пожаловать!',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[register_user]
    #     )
    #     return super().form_valid(form)

    def form_valid(self, form):
        register_user = form.save()
        # register_user['is_active'] = False
        returnVal = super(RegisterView, self).form_valid(form)
        send_email(register_user)
        return returnVal
