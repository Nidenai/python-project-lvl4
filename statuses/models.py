from django.db import models

class Statuses(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Имя')
    status_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
