from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *
from .models import *


class TaskPage(TemplateView):
    template_name = 'tasks.html'

    def get(self, request):
        tasks = Tasks.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, self.template_name, context)


class LabelPage(TemplateView):
    template_name = 'labels.html'

    def get(self, request):
        labels = Labels.objects.all()
        context = {
            'labels': labels
        }
        return render(request, self.template_name, context)


class AddTask(TemplateView):
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


class AddLabel(TemplateView):
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