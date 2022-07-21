from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from task_manager.mixins import CustomLoginRequiredMixin
from .forms import LabelForm
from .models import Labels


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
    fields = ['name']
    success_url = reverse_lazy('labels:list')
    success_message = _('Label update succesfully')


class LabelDelete(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete.html'
    model = Labels
    success_url = reverse_lazy('labels:list')
    success_message = _('Label delete succesfully')
    msg_error = _('Невозможно удалить метку, потому что она используется')

    def form_valid(self, form):
        if self.get_object().labels.all():
            messages.error(self.request, self.msg_error)
        else:
            super(LabelDelete, self).form_valid(form)
        return redirect(self.success_url)
