from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, FormView, CreateView

from task_manager.mixins import CustomDeleteView
from .forms import *
from .models import *


class StatusPage(LoginRequiredMixin, ListView):
    template_name = 'statuses/statuses.html'
    model = Statuses
    context_object_name = 'statuses'

    def dispatch(self, request, *args, **kwargs):
        self.redirect_url_while_restricted = 'login'
        self.restriction_message = _('You are not authorized! Please sign in.')
        return super().dispatch(request, *args, **kwargs)


class AddStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/add_status.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list')
    success_message = _('Status created succesfully')

    def dispatch(self, request, *args, **kwargs):
        self.redirect_url_while_restricted = 'login'
        self.restriction_message = _('You are not authorized! Please sign in.')
        return super().dispatch(request, *args, **kwargs)


class StatusUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/status_update.html'
    model = Statuses
    fields = ['status_name']
    success_url = reverse_lazy('statuses:list')

    def dispatch(self, request, *args, **kwargs):
        self.redirect_url_while_restricted = 'login'
        self.restriction_message = _('You are not authorized! Please sign in.')
        return super().dispatch(request, *args, **kwargs)


class StatusDelete(LoginRequiredMixin, CustomDeleteView):
    template_name = 'statuses/status_delete.html'
    model = Statuses
    success_url = reverse_lazy('statuses:list')
    success_message = 'Статус удален успешно'
    unsuccess_message = 'Статус нельзя удалить, потому что он используется'

    def dispatch(self, request, *args, **kwargs):
        self.redirect_url_while_restricted = 'login'
        self.restriction_message = _('You are not authorized! Please sign in.')
        return super().dispatch(request, *args, **kwargs)
