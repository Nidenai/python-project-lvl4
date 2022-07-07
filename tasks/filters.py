from django import forms
from django.db.models import Value
from django.db.models.functions import Concat
from django_filters import FilterSet, BooleanFilter, ChoiceFilter
from django.utils.translation import gettext as _
from labels.models import Labels
from statuses.models import Status
from tasks.models import Tasks
from users.models import User


class TaskFilter(FilterSet):
    statuses = Status.objects.values_list('id', 'status_name', named=True).all()
    labels = Labels.objects.values_list('id', 'label_name', named=True).all()
    users = User.objects.values_list(
        'id', Concat('first_name', Value(' '), 'last_name'), named=True
    ).all()
    status = ChoiceFilter(label=_('Status'), choices=statuses)
    assigned_user = ChoiceFilter(label=_('Executor'), choices=users)
    label = ChoiceFilter(label=_('Label'), choices=labels)
    self_task = BooleanFilter(label=_('Only my tasks'),
                              widget=forms.CheckboxInput,
                              method='filter_self',
                              )

    def filter_self(self, queryset, name, value):
        if value:
            author = getattr(self.request, 'user', None)
            queryset = queryset.filter(assigned_user=author)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'assigned_user', 'label', 'self_task']
