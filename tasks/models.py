from django.db import models
from labels.models import Labels
from statuses.models import Statuses


class Tasks(models.Model):

    title = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    task_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    label = models.ForeignKey(Labels, on_delete=models.CASCADE, verbose_name='Метка')
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE, verbose_name='Статусы')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'