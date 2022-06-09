from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from task_manager.mixins import CustomAddForm
from .forms import *
from .models import *


class StatusPage(ListView):
    template_name = 'statuses/statuses.html'
    queryset = Statuses.objects.order_by('id')
    context_object_name = 'statuses'


class AddStatus(CustomAddForm):
    template_name = 'statuses/add_status.html'
    form_to_post = StatusForm
    model = Statuses
    redirect_to = 'statuses'


class StatusUpdate(UpdateView):
    template_name = 'statuses/status_update.html'
    model = Statuses
    fields = ['status_name']
    success_url = reverse_lazy('statuses')


class StatusDelete(SuccessMessageMixin, DeleteView):
    template_name = 'statuses/status_delete.html'
    model = Statuses
    success_url = reverse_lazy('statuses')
    success_message = 'Статус удален успешно'
    unsuccess_message = 'Статус нельзя удалить, потому что он используется'

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, self.unsuccess_message)
            return redirect(self.success_url)
        else:
            messages.success(self.request, self.success_message)
            return redirect(self.success_url)

