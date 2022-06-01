from django.db import models

class Labels(models.Model):
    label_name = models.CharField(max_length=50, verbose_name='Имя')
    label_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

class Tasks(models.Model):

    title = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    task_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    mark = models.ForeignKey(Labels, on_delete=models.CASCADE, verbose_name='Метка')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'