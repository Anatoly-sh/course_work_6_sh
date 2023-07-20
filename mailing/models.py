from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email_contact = models.EmailField(max_length=150, unique=True, verbose_name='Адрес клиента')
    full_name = models.CharField(max_length=150, verbose_name='Полное имя', **NULLABLE)
    comment = models.TextField(max_length=2000, verbose_name='Комментарии', **NULLABLE)
    # author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)

    def __str__(self):
        return self.email_contact

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Message(models.Model):
    letter_subject = models.CharField(max_length=150, verbose_name='Тема письма')
    letter_body = models.TextField(max_length=2000, verbose_name='Текст письма')

    def __str__(self):
        return self.letter_subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailSetting(models.Model):
    choices_period = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    mailing_status = [
        ('created', 'Создана'),
        ('launched', 'Запущена'),
        ('completed', 'Завершена')
    ]

    mailing_start = models.DateTimeField(verbose_name='Начало рассылки', **NULLABLE)
    mailing_stop = models.DateTimeField(verbose_name='Конец рассылки', **NULLABLE)
    mailing_period = models.CharField(max_length=10, choices=choices_period, verbose_name='Периодичность', **NULLABLE)
    status = models.CharField(max_length=10, choices=mailing_status, verbose_name='Статус рассылки', **NULLABLE)
    # author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    destination = models.ManyToManyField(Client, verbose_name='Клиент')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)
    launched_date = models.DateField(verbose_name='Дата отправки рассылки', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активация рассылки')

    def __str__(self):
        return f'{self.message} / {self.status}'

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'
        # permissions = ['can_deactivate_setting',
        #                'Can deactivate setting'
        #                ]


class Attempt(models.Model):
    status = [
        ('delivered', 'доставлено'),
        ('not_delivered', 'не доставлено')
    ]
    attempt = models.ForeignKey(MailSetting, on_delete=models.CASCADE, verbose_name='Попытка', **NULLABLE)
    attempt_time = models.DateTimeField(verbose_name='Дата попытки', **NULLABLE)
    attempt_status = models.CharField(choices=status, max_length=50, verbose_name='Статус попытки', **NULLABLE)
    server_answer = models.CharField(max_length=100, verbose_name='Ответ сервера', **NULLABLE)

    def __str__(self):
        return self.attempt

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
