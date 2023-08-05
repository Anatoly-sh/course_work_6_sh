from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView, UpdateView

from blog.models import Blog
from mailing.form import ClientForm, MailSettingForm
from mailing.models import Client, MailSetting, Attempt


class ClientList(LoginRequiredMixin, ListView):
    model = Client

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.has_perm('mailing.view_client'):
    #         return queryset
    #     return Client.objects.filter(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset
        return Client.objects.filter(author=self.request.user)


class ClientDetail(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user  # запись в таблицу Client автора записи
        return super().form_valid(form)


class ClientUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def test_func(self):
        """
        Проверка (UserPassesTestMixin) является ли текущий пользователь автором клиента сервиса
        """
        obj = self.get_object()
        return self.request.user == obj.author

    def get_success_url(self, *args, **kwargs):
        return reverse('mailing:client_detail', args=[self.get_object().pk])


class ClientDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')

    def test_func(self):
        """
        Проверка (UserPassesTestMixin) является ли текущий пользователь автором клиента сервиса
        """
        obj = self.get_object()
        return self.request.user == obj.author
# ---------------------------------------------------------------------------------------


class MailSettingList(LoginRequiredMixin, ListView):
    model = MailSetting

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser:
            return queryset.order_by('-mailing_start')
        return MailSetting.objects.filter(author=self.request.user).order_by('-mailing_start')


class MailSettingDetail(LoginRequiredMixin, DetailView):
    model = MailSetting

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.has_perm('mailing.view_mailsetting'):
    #         return queryset
    #     return MailSetting.objects.filter(author=self.request.user)


class MailSettingCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MailSetting
    form_class = MailSettingForm
    success_url = reverse_lazy('mailing:mail-setting-list')

    def test_func(self):
        """
        Проверка, что текущий пользователь не входит в группу managers
        """
        return not self.request.user.groups.filter(name='managers').exists()

    def form_valid(self, form):
        instance = form.save()
        instance.author = self.request.user  # запись в таблицу Client автора записи
        return super().form_valid(form)


class MailSettingUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MailSetting
    form_class = MailSettingForm

    def test_func(self):
        """
        Проверка (UserPassesTestMixin) является ли текущий пользователь автором рассылки
        и не находится в группе managers
        """
        obj = self.get_object()
        return self.request.user == obj.author
               # and not self.request.user.groups.filter(name='managers').exists()

    def get_success_url(self, *args, **kwargs):
        return reverse('mailing:mail-setting-detail', args=[self.get_object().pk])


class MailSettingDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailSetting
    success_url = reverse_lazy('mailing:mail-setting-list')

    def test_func(self):
        """
        Проверка (UserPassesTestMixin) является ли текущий пользователь автором рассылки
        и не находится в группе managers
        """
        obj = self.get_object()
        return self.request.user == obj.author
               # and not self.request.user.groups.filter(name='managers').exists()
# ---------------------------------------------------------------------------------------


class AttemptView(LoginRequiredMixin, ListView):
    model = Attempt


class MainPage(TemplateView):
    """Главная страница"""
    template_name = 'mailing/index.html'

    def get_context_data(self, **kwargs):
        blog = Blog.objects.order_by('?')[:3]  # выборка из БД Blog 3 случайных статьи
        uniq_clients_count = len(Client.objects.all().distinct('email_contact'))    # уникальные клиенты по почте
        settings_count = len(MailSetting.objects.all())                             # подсчёт кол-во рассылок
        settings_active = len(MailSetting.objects.filter(status='launched'))        # подсчёт кол-во активных рассылок
        context = super().get_context_data()
        context['settings_count'] = settings_count
        context['settings_active'] = settings_active
        context['clients_count'] = uniq_clients_count
        context['blogs_3'] = blog

        return context


# @permission_required(perm='mailing.can_deactivate_mailing')
def toggle_activity_mailing(request, pk):
    """ Функция блокировки (переключения активности) рассылки"""
    selected_mailing = get_object_or_404(MailSetting, pk=pk)
    if selected_mailing.is_active:
        selected_mailing.is_active = False
    else:
        selected_mailing.is_active = True
    selected_mailing.save()

    return redirect(reverse('mailing:mail-setting-list'))

