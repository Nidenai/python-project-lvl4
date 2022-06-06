from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from .forms import *
from .models import *


class LabelPage(ListView):
    template_name = 'labels/labels.html'
    queryset = Labels.objects.order_by('id')
    context_object_name = 'labels'


class AddLabel(View):
    template_name = 'labels/add_label.html'

    def get(self, request):
        context = {
            'form': LabelForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LabelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('labels')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class LabelUpdate(UpdateView):
    template_name = 'labels/label_update.html'
    model = Labels
    fields = ['label_name']
    success_url = reverse_lazy('labels')

class LabelDelete(DeleteView):
    template_name = 'labels/label_delete.html'
    model = Labels
    success_url = reverse_lazy('labels')