from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from users.forms import UserCreationForm
from users.models import User


class Register(View):
    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class UserList(ListView):
    queryset = User.objects.order_by('id')
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserUpdate(UpdateView):
    template_name = 'users/user_update.html'
    model = User
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('users')

class UserDelete(DeleteView):
    template_name = 'users/user_delete.html'
    model = User
    success_url = reverse_lazy('users')