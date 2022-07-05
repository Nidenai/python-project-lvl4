from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, FormView, CreateView

from task_manager.mixins import CustomDeleteView
from .forms import *
from .models import *


class StatusPage(ListView):
    template_name = 'statuses/statuses.html'
    queryset = Statuses.objects.order_by('id')
    context_object_name = 'statuses'


class AddStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/add_status.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status created succesfully')


class StatusUpdate(UpdateView):
    template_name = 'statuses/status_update.html'
    model = Statuses
    fields = ['status_name']
    success_url = reverse_lazy('statuses')


class StatusDelete(CustomDeleteView):
    template_name = 'statuses/status_delete.html'
    model = Statuses
    success_url = reverse_lazy('statuses')
    success_message = 'Статус удален успешно'
    unsuccess_message = 'Статус нельзя удалить, потому что он используется'
