python manage.py send_command

python manage.py crontab add
python manage.py crontab remove


https://github.com/LeoneBacciu/django-email-verification
def verified_callback(user):
    user.is_active = True

В settings.py:
EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = 'noreply@aliasaddress.com'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'mail_body.html'
EMAIL_MAIL_PLAIN = 'mail_body.txt'
EMAIL_MAIL_TOKEN_LIFE = 60 * 60
EMAIL_MAIL_PAGE_TEMPLATE = 'confirm_template.html'
EMAIL_PAGE_DOMAIN = 'http://mydomain.com/'
EMAIL_MULTI_USER = True  # optional (defaults to False)

В деталях:

EMAIL_VERIFIED_CALLBACK: функция, которая будет вызываться, когда пользователь успешно 
подтвердит электронную почту. Принимает пользовательский объект в качестве аргумента.
EMAIL_FROM_ADDRESS: это может быть то же самое EMAIL_HOST_USERили псевдоним адреса, если 
требуется.
EMAIL_MAIL_:
    SUBJECT: тема письма по умолчанию.
    HTML: шаблон тела письма в формате html.
    PLAIN: шаблон тела письма в виде файла .txt.
EMAIL_TOKEN_LIFE: срок жизни ссылки электронной почты (в секундах).
EMAIL_PAGE_TEMPLATE: шаблон просмотра успеха/ошибки.
EMAIL_PAGE_DOMAIN: домен ссылки для подтверждения (обычно это домен вашего сайта).
EMAIL_MULTI_USER: (необязательно), если True ошибка не будет выдана при наличии нескольких 
пользователей с одинаковым адресом электронной почты (будет активирован только один)


EMAIL_VERIFIED_CALLBACK может быть функцией в AUTH_USER_MODEL, например:

EMAIL_VERIFIED_CALLBACK = get_user_model().verified_callback