# Generated by Django 4.2.3 on 2023-07-30 14:41

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активный статус'),
        ),
    ]