# Generated by Django 4.2.3 on 2023-08-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_active_user', 'Blocing user')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активный статус'),
        ),
    ]
