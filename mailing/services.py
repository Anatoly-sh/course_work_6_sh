from django.core.mail import send_mail

from mailing.management.commands.send_command import Command, mailing_subject_renew, \
    mailing_subject_select_for_command_handle, mailing_and_statistic
# from config import settings
from mailing.models import *


def send_auto(*args):
    # ------------------------------------------------------
    auto_attr = args[0]
    with open("scheduled_job.log", "a") as f:  # append mode
        f.write(str(auto_attr))
        f.write(' - сюда пишет send_auto\n')
    # ------------------------------------------------------
    # Command.handle(auto_attr)


    # ------------------------------------------------------
    mailing_subject_renew()               # обновление флагов рассылок в БД
    # active_mailings = mailing_subject_select_for_command_handle(auto_attr)  # выбор действующих рассылок
    #(флаги is_active и launched)+send_auto
    with open("scheduled_job.log", "a") as f:  # append mode
        # f.write(str(len(active_mailings)))
        f.write(' - сюда пишет send_auto\n')
    # mailing_and_statistic(active_mailings)
    # ------------------------------------------------------




    # email_s = []  # список почтовых адресов клиентов для рассылки
    # for client in Client.objects.all():  # отфильтровать клиентов пользователя!!!
    #     email_s.append(str(client.email_contact))
    #     # print(client.email_contact)
    #
    # for mailing in MailSetting.objects.all():  # перебор рассылок
    #     mess = mailing.message
    #     print(mess)
    #     message_obj = Message.objects.filter(letter_subject=mess)
    #     for mess in message_obj:  # для каждой рассылки
    #         print(mess.letter_subject)
    #         print(mess.letter_body)
    #         print(mailing.status)
    #         print('---------------------------------------')
            # send_mail(
            #     subject=mess.letter_subject,
            #     message=mess.letter_body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[*email_s],
            #     fail_silently=False,
            # )
