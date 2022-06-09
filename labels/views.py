from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from task_manager.mixins import CustomAddForm
from .forms import *
from .models import *


class LabelPage(ListView):
    template_name = 'labels/labels.html'
    queryset = Labels.objects.order_by('id')
    context_object_name = 'labels'


class AddLabel(CustomAddForm):
    template_name = 'labels/add_label.html'
    form_to_post = LabelForm
    model = Labels
    redirect_to = 'labels'


class LabelUpdate(UpdateView):
    template_name = 'labels/label_update.html'
    model = Labels
    fields = ['label_name']
    success_url = reverse_lazy('labels')

class LabelDelete(DeleteView):
    template_name = 'labels/label_delete.html'
    model = Labels
    success_url = reverse_lazy('labels')