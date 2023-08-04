from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView, ListView
from django_email_verification import send_email

from config import settings
from mailing.models import MailSetting
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
        register_user.is_active = False
        returnVal = super(RegisterView, self).form_valid(form)
        send_email(register_user)
        return returnVal


class UserListView(LoginRequiredMixin, ListView):
    model = User

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.groups.filter(name='managers').exists() or self.request.user.is_superuser:
            return queryset.order_by('email')
        print(queryset)
        return queryset.filter(email=self.request.user)     # выводит только себя


@permission_required(perm='users.set_active_user')
def toggle_activity_user(request, pk):
    """ Функция блокировки (переключения активности) пользователя"""
    selected_user = get_object_or_404(User, pk=pk)
    if selected_user.is_active:
        selected_user.is_active = False
    else:
        selected_user.is_active = True
    selected_user.save()

    return redirect(reverse('users:users-list'))
