from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import *
from .models import *


class LabelPage(ListView):
    template_name = 'labels.html'
    queryset = Labels.objects.order_by('id')
    context_object_name = 'labels'


class AddLabel(View):
    template_name = 'add_label.html'

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
