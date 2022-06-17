from django.db import models
from django.utils.translation import gettext_lazy as _

from labels.models import Labels
from statuses.models import Statuses
from users.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    task_date = models.DateTimeField(auto_now=True, verbose_name=_('Date'))
    label = models.ManyToManyField(Labels, verbose_name=_('Label'), related_name='labels')
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, verbose_name=_('Status'))
    created_user = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT, null=True,
                                     verbose_name=_('Author'))
    assigned_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor',
                                      verbose_name=_('Executor'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.title
