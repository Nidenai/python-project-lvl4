from django.db import models
from django.utils.translation import gettext_lazy as _


class Labels(models.Model):
    label_name = models.CharField(max_length=50, verbose_name=_('Name'), unique=True)
    label_date = models.DateTimeField(auto_now=True, verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')

    def __str__(self):
        return self.label_name
