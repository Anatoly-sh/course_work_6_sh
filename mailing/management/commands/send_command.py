from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

# from config import settings         # проверить
from mailing.models import *


def mailing_subject_select_for_crontab():
    tmp_mailing = mailing_subject_select_for_command_handle()
    return tmp_mailing.filter()


def mailing_subject_select_for_command_handle():
    """
    Из всех рассылок БД выбор активных & запущенных (launched).
    """
    activ_mailing = MailSetting.objects.all().filter(is_active=True, status='launched')
    return activ_mailing


def mailing_and_statistic(mailing_queryset):
    global letter_subject, letter_body
    pk_list = []                            # получение перечня ID для отправки каждого из писем mailing_queryset
    for m_q in mailing_queryset:
        pk_list.append(m_q.pk)
    for pk in pk_list:                      # перебор писем для отправки через ID
        mailing = mailing_queryset.get(pk=pk)
        client_list = []                    # получение перечня клиентов для отправки каждого из писем mailing_queryset
        for cl in mailing.client.all():
            client_list.append(cl.email_contact)
        # print(client_list)
        # print(pk)
        message_obj = Message.objects.filter(letter_subject=mailing.message)
        for mess in message_obj:                # выбор предмета рассылки для каждой рассылки
            letter_subject = mess.letter_subject
            letter_body = mess.letter_body
        # print(letter_subject)
        # print(letter_body)
        status_list = []
        try:
            send_mail(
                subject=letter_subject,
                message=letter_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[*client_list],
                fail_silently=False,
            )
        except Exception as exp:
            server_response = {'attempt_status': Attempt.NOT_DELIVERED,
                               'server_answer': 'Ошибка при отправке сообщения: {}'.format(str(exp)),
                               'attempt': MailSetting.objects.get(pk=pk)}
            status_list.append(Attempt(**server_response))
        else:
            server_response = {'attempt_status': Attempt.DELIVERED,
                               'server_answer': 'Сообщение успешно отправлено',
                               'attempt': MailSetting.objects.get(pk=pk)}
            status_list.append(Attempt(**server_response))

        Attempt.objects.bulk_create(status_list)


        # print(letter_subject)
        # print(letter_body)
        # print(settings.EMAIL_HOST_USER)
        # print([*client_list])

def mailing_subject_renew():
    """
    Изменение флагов перечня рассылок в соответствии с текущей датой.
    """
    for mailing in MailSetting.objects.all().filter(is_active=True):  # перебор рассылок

        if datetime.now().timestamp() <= mailing.mailing_start.timestamp():
            mailing.status = 'created'
        else:
            if datetime.now().timestamp() <= mailing.mailing_stop.timestamp():
                mailing.status = 'launched'
            else:
                mailing.status = 'completed'
        mailing.save()


class Command(BaseCommand):
    help = 'Команда инициирует разовую рассылку по всем заданным параметрам объекта MailSetting'

    @staticmethod
    def handle(*args, **options):
        # ------------------------------------------------------
        with open("scheduled_job_handle.log", "a") as f:  # append mode
            # f.write(*args)
            f.write(' - это handle\n')
        # ------------------------------------------------------

        mailing_subject_renew()  # обновление флагов рассылок в БД
        active_mailing = mailing_subject_select_for_command_handle()    # выбор действующих рассылок
                                                                        # (флаги is_active и launched)
        mailing_and_statistic(active_mailing)
# ------------------------------------------------------


