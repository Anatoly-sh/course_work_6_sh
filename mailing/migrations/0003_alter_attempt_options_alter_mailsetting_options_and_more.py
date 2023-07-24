# Generated by Django 4.2.3 on 2023-07-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_alter_mailsetting_destination'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attempt',
            options={'verbose_name': 'Попытка рассылки', 'verbose_name_plural': 'Попытки рассылок'},
        ),
        migrations.AlterModelOptions(
            name='mailsetting',
            options={'verbose_name': 'Рассылка: параметры', 'verbose_name_plural': 'Рассылки: параметры'},
        ),
        migrations.RenameField(
            model_name='mailsetting',
            old_name='destination',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Комментарии'),
        ),
    ]