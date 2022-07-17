from django.db import models
from django.utils.translation import gettext_lazy as _

from labels.models import Labels
from statuses.models import Status
from users.models import User


class Tasks(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    description = models.TextField(max_length=500, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date'))
    labels = models.ManyToManyField(Labels, verbose_name=_('Label'), blank=True, related_name='labels')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('Status'))
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT, null=True,
                               verbose_name=_('Author'))
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor',
                                 verbose_name=_('Executor'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.name
