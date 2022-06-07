from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, FormView

from .forms import *
from .models import *


class TaskPage(ListView):
    template_name = 'tasks/tasks.html'
    queryset = Tasks.objects.order_by('id')
    context_object_name = 'tasks'


class AddTask(FormView):
    template_name = 'tasks/add_task.html'
    form_class = TaskForm
    success_url = '/tasks'

    def form_valid(self, form):
        task_form = form.save()
        task_form.created_user.add(self.request.username)
        task_form.save()
        return super().form_valid(form)



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