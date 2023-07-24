from django.core.mail import send_mail

from mailing.management.commands.send_command import Command
# from config import settings
from mailing.models import *


def email_test(*args):
    # ------------------------------------------------------
    with open("scheduled_job.log", "a") as f:  # append mode
        f.write(*args)
        f.write(' - начало цикла\n')
    # ------------------------------------------------------
    Command.handle(*args)
    email_s = []  # список почтовых адресов клиентов для рассылки
    for client in Client.objects.all():  # отфильтровать клиентов пользователя!!!
        email_s.append(str(client.email_contact))
        # print(client.email_contact)

    for mailing in MailSetting.objects.all():  # перебор рассылок
        mess = mailing.message
        print(mess)
        message_obj = Message.objects.filter(letter_subject=mess)
        for mess in message_obj:  # для каждой рассылки
            print(mess.letter_subject)
            print(mess.letter_body)
            print(mailing.status)
            print('---------------------------------------')
            # send_mail(
            #     subject=mess.letter_subject,
            #     message=mess.letter_body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[*email_s],
            #     fail_silently=False,
            # )
