from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import *
from .models import *


class StatusPage(ListView):
    template_name = 'statuses/statuses.html'
    queryset = Statuses.objects.order_by('id')
    context_object_name = 'statuses'


class AddStatus(View):
    template_name = 'statuses/add_status.html'

    def get(self, request):
        context = {
            'form': StatusForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = StatusForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('statuses')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
