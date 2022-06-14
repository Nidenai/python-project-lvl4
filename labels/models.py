from django.db import models

class Labels(models.Model):
    label_name = models.CharField(max_length=50, verbose_name='Имя', unique=True)
    label_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

    def __str__(self):
        return self.label_name
