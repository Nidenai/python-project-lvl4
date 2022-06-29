from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, FormView

from task_manager.mixins import HandleNoPermissionMixin
from .filters import *
from .forms import *


class TaskPage(LoginRequiredMixin, ListView):
    template_name = 'tasks/tasks.html'
    queryset = Tasks.objects.order_by('id')
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET, queryset=self.get_queryset())
        return context


class AddTask(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'tasks/add_task.html'
    form_class = TaskForm
    success_url = '/tasks'
    success_message = _('Task created succesfully')

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


class TaskUpdate(LoginRequiredMixin, HandleNoPermissionMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    model = Tasks
    fields = ['title', 'description', 'label', 'status']
    success_url = reverse_lazy('tasks')
    success_message = _('Task changed successfully')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_user

    def dispatch(self, request, *args, **kwargs):
        self.redirect_url_while_restricted = 'tasks'
        self.restriction_message = _("Only the author of that task can edit a task!")
        return super().dispatch(request, *args, **kwargs)


class TaskDelete(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Tasks
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted successfully')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.created_user

    def dispatch(self, request, *args, **kwargs):
        self.redirect_url_while_restricted = 'tasks'
        self.restriction_message = _("Only the author of that task can delete a task!")
        return super().dispatch(request, *args, **kwargs)
