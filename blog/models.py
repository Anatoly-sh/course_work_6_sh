from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(max_length=2000, verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    views_number = models.IntegerField(verbose_name='Количество просмотров')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('-published_date',)
