from blog.models import Blog
from mailing.management.commands.send_command import Command, mailing_subject_renew, \
    mailing_subject_select_for_command_handle, mailing_and_statistic, db_test
from django.conf import settings
from django.core.cache import cache


def send_auto(*args):
    # ------------------------------------------------------
    # auto_attr = args[0]
    with open("scheduled_job.log", "a") as f:  # append mode
        # f.write(str(auto_attr))
        f.write(' - сюда пишет send_auto1\n')
    # ------------------------------------------------------
    # Command.handle(auto_attr)
    db_test()

    # ------------------------------------------------------
    mailing_subject_renew()               # обновление флагов рассылок в БД
    # ------------------------------------------------------
    auto_attr = args[0]
    with open("scheduled_job.log", "a") as f:  # append mode
        f.write(str(auto_attr))
        f.write(' - сюда пишет send_auto2\n')
    # ------------------------------------------------------
    active_mailings = mailing_subject_select_for_command_handle(auto_attr)  # выбор действующих рассылок
    #(флаги is_active и launched)+send_auto
    with open("scheduled_job.log", "a") as f:  # append mode
        # f.write(str(len(active_mailings)))
        f.write(' - сюда пишет send_auto3\n')
    mailing_and_statistic(active_mailings)
    # ------------------------------------------------------


def get_cached_blog_view():
    """Низкоуровневое кеширование"""
    data = Blog.objects.all()
    if settings.CACHE_ENABLED:
        key = 'blog_list'
        blog_list = cache.get(key)
        if blog_list is None:
            blog_list = data
            cache.set(key, blog_list)
        return blog_list
    return data
