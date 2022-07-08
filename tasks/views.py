from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import UpdateView, DeleteView, FormView
from django_filters.views import FilterView

from task_manager.mixins import HandleNoPermissionMixin
from .filters import *
from .forms import *


class TaskPage(LoginRequiredMixin, FilterView):
    template_name = 'tasks/list.html'
    model = Tasks
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class AddTask(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'create.html'
    form_class = TaskForm
    success_url = '/tasks'
    success_message = _('Task created succesfully')

    def form_valid(self, form):
        task_form = form.save()
        task_form.created_user = self.request.user
        task_form.save()
        return super().form_valid(form)


class TaskDescription(View):
    template_name = 'tasks/detail.html'

    def get(self, request, task_id):
        task = Tasks.objects.get(pk=task_id)
        context = {
            'task': task
        }
        return render(request, self.template_name, context)


class TaskUpdate(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UpdateView):
    template_name = 'update.html'
    model = Tasks
    fields = ['title', 'description', 'label', 'status']
    success_url = reverse_lazy('tasks')
    success_message = _('Task changed successfully')



class TaskDelete(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    template_name = 'delete.html'
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
