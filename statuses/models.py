from django.db import models
from django.utils.translation import gettext_lazy as _

class Statuses(models.Model):
    status_name = models.CharField(max_length=50, verbose_name=_('Name'), unique=True)
    status_date = models.DateTimeField(auto_now=True, verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')

    def __str__(self):
        return self.status_name
