from django.db import models

from labels.models import Labels
from statuses.models import Statuses
from users.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    task_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    label = models.ForeignKey(Labels, on_delete=models.PROTECT, verbose_name='Метка')
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, verbose_name='Статусы')
    created_user = models.ForeignKey(User, related_name='Автор', on_delete=models.PROTECT, null=True)
    assigned_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Исполнитель')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
