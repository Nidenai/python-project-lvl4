from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, FormView

from .forms import *
from .models import *
from .filters import *

class TaskPage(LoginRequiredMixin, ListView):
    template_name = 'tasks/tasks.html'
    queryset = Tasks.objects.order_by('id')
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET, queryset=self.get_queryset())
        return context



class AddTask(LoginRequiredMixin, FormView):
    template_name = 'tasks/add_task.html'
    form_class = TaskForm
    success_url = '/tasks'


    def form_valid(self, form):
        task_form = form.save()
        task_form.created_user = self.request.user
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

class TaskUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    model = Tasks
    fields = ['title', 'description', 'label', 'status']
    success_url = reverse_lazy('tasks')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_user

class TaskDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Tasks
    success_url = reverse_lazy('tasks')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_user