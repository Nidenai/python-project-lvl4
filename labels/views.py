from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, CreateView

from task_manager.mixins import CustomDeleteView, CustomLoginRequiredMixin
from .forms import *
from .models import *


class LabelPage(CustomLoginRequiredMixin, ListView):
    template_name = 'labels/list.html'
    queryset = Labels.objects.order_by('id')
    context_object_name = 'labels'


class AddLabel(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'create.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels:list')
    success_message = _('Label created succesfully')


class LabelUpdate(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'update.html'
    model = Labels
    fields = ['label_name']
    success_url = reverse_lazy('labels:list')
    success_message = _('Label update succesfully')


class LabelDelete(CustomLoginRequiredMixin, CustomDeleteView):
    template_name = 'delete.html'
    model = Labels
    success_url = reverse_lazy('labels:list')
    success_message = _('Label delete succesfully')
