from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, CreateView

from task_manager.mixins import CustomDeleteView, CustomLoginRequiredMixin
from .forms import *
from .models import *


class StatusPage(CustomLoginRequiredMixin, ListView):
    template_name = 'statuses/statuses.html'
    model = Statuses
    context_object_name = 'statuses'


class AddStatus(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/add_status.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status created succesfully')


class StatusUpdate(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/status_update.html'
    model = Statuses
    fields = ['status_name']
    success_url = reverse_lazy('statuses:list')


class StatusDelete(CustomLoginRequiredMixin, CustomDeleteView):
    template_name = 'statuses/status_delete.html'
    model = Statuses
    success_url = reverse_lazy('statuses:list')
    success_message = 'Статус удален успешно'
    unsuccess_message = 'Статус нельзя удалить, потому что он используется'
