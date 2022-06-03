from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import *
from .models import *


class TaskPage(ListView):
    template_name = 'tasks.html'
    queryset = Tasks.objects.order_by('id')
    context_object_name = 'tasks'


class AddTask(View):
    template_name = 'add_task.html'

    def get(self, request):
        context = {
            'form': TaskForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tasks')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class TaskDescription(View):
    template_name = 'task_description.html'

    def get(self, request, task_id):
        task = Tasks.objects.get(pk=task_id)
        context = {
            'task': task
        }
        return render(request, self.template_name, context)
