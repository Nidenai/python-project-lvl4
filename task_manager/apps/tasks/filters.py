from django import forms
from django.utils.translation import gettext as _
from django_filters import FilterSet, BooleanFilter, ModelChoiceFilter

from task_manager.apps.tasks.models import Tasks
from task_manager.apps.labels.models import Labels


class TaskFilter(FilterSet):
    labels = ModelChoiceFilter(label=_('Label_one'),
                               queryset=Labels.objects.all())
    self_task = BooleanFilter(label=_('Only my tasks'),
                              widget=forms.CheckboxInput,
                              method='filter_self',
                              )

    def filter_self(self, queryset, name, value):
        if value:
            author = getattr(self.request, 'user', None)
            queryset = queryset.filter(author=author)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels', 'self_task']
