from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

# from config import settings         # проверить
from mailing.models import *


# def mailing_subject_select_for_crontab():
#     tmp_mailing = mailing_subject_select_for_command_handle()
#     return tmp_mailing.filter()


def mailing_subject_select_for_command_handle(freq):
    """
    Из всех рассылок БД выбор активных & запущенных (launched). После - фильтрация авторассылок.
    """
    activ_mailing = MailSetting.objects.all().filter(is_active=True, status='launched')
    if freq == 'Раз в день':
        activ_mailing.filter(mailing_period='daily')  # daily
    elif freq == 'Раз в неделю':
        activ_mailing.filter(mailing_period='Раз в неделю')  # weekly
    elif freq == 'Раз в месяц':
        activ_mailing.filter(mailing_period='Раз в месяц')  # monthly
    # ------------------------------------------------------
    with open("scheduled_job_handle.log", "a") as f:  # append mode
        f.writelines(f'{str(len(activ_mailing))}\n{str(freq)}\n{str(activ_mailing)}\n'
                     f'- это mailing_subject_select_for_command_handle')
    # ------------------------------------------------------
    return activ_mailing


def mailing_and_statistic(mailing_queryset):  # получен queryset рассылок
    global letter_subject, letter_body
    pk_list = []  # получение перечня pk каждой рассылки из mailing_queryset
    for m_q in mailing_queryset:
        pk_list.append(m_q.pk)

    for pk in pk_list:          # перебор рассылок через pk, определение параметров и отправка
        mailing = mailing_queryset.get(pk=pk)

        client_list = []        # получение перечня клиентов для отправки
        # каждой рассылки из mailing_queryset
        for cl in mailing.client.all():
            client_list.append(cl.email_contact)
        print(client_list)
        print(pk)

        message_obj = Message.objects.filter(letter_subject=mailing.message)    # queryset из 1 объекта
        letter_subject = message_obj[0].letter_subject          # тема письма
        letter_body = message_obj[0].letter_body                # тело письма

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
    datetime_now = datetime.now().timestamp()
    for mailing in MailSetting.objects.all().filter(is_active=True):  # перебор рассылок
        if datetime_now <= mailing.mailing_start.timestamp():
            mailing.status = 'created'
        else:
            if datetime_now <= mailing.mailing_stop.timestamp():
                mailing.status = 'launched'
            else:
                mailing.status = 'completed'


def hhh(args):
    if not args:
        print("List is empty")
    # ------------------------------------------------------
    with open("scheduled_job_handle.log", "a") as f:  # append mode
        f.write(str(args))
        f.write(' - это handle2\n')
    # ------------------------------------------------------


class Command(BaseCommand):
    help = 'Команда инициирует разовую рассылку по всем заданным параметрам объекта MailSetting'

    @staticmethod
    def handle(*args, **options):
        if not args:                # не пришел аргумент из авторассылки?
            send_auto = None
        else:
            send_auto = args[0]     # пришел аргумент из авторассылки, передаем в параметре
        # hhh(send_auto)
        # ------------------------------------------------------

        mailing_subject_renew()  # обновление флагов рассылок в БД
        active_mailings = mailing_subject_select_for_command_handle(send_auto)  # выбор действующих рассылок
        # (флаги is_active и launched)+send_auto
        mailing_and_statistic(active_mailings)
# ------------------------------------------------------
