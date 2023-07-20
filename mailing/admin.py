from django.contrib import admin

from mailing.models import Client, Message, MailSetting, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email_contact', 'full_name', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'letter_body')


@admin.register(MailSetting)
class MailSettingAdmin(admin.ModelAdmin):
    list_display = ('mailing_start', 'mailing_stop', 'mailing_period', 'status',
                    'message', 'launched_date', 'is_active')


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'attempt_time', 'attempt_status', 'server_answer')
