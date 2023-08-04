# Generated by Django 4.2.3 on 2023-08-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(max_length=2000, verbose_name='Содержимое статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('views_number', models.IntegerField(verbose_name='Количество просмотров')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
                'ordering': ('-published_date',),
            },
        ),
    ]
