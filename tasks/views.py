from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from .forms import *
from .models import *


class TaskPage(ListView):
    template_name = 'tasks/tasks.html'
    queryset = Tasks.objects.order_by('id')
    context_object_name = 'tasks'


class AddTask(View):
    template_name = 'tasks/add_task.html'

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
    template_name = 'tasks/task_description.html'

    def get(self, request, task_id):
        task = Tasks.objects.get(pk=task_id)
        context = {
            'task': task
        }
        return render(request, self.template_name, context)

class TaskUpdate(UpdateView):
    template_name = 'tasks/task_update.html'
    model = Tasks
    fields = ['title', 'description', 'label', 'status']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Tasks
    success_url = reverse_lazy('tasks')