from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from task_manager.mixins import HandleNoPermissionMixin
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
            messages.success(request, _('User register successful'))
            return redirect('login')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class UserList(ListView):
    queryset = User.objects.order_by('id')
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserUpdate(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    template_name = 'users/user_update.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = _('User changed successfully')
    restriction_message = _('NO')
    redirect_url_while_restricted = reverse_lazy('users')

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('users')


class UserDelete(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    template_name = 'users/user_delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User deleted successfully')
    restriction_message = _('NO')
    redirect_url_while_restricted = 'users'

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id



class CustomLogin(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = _('You are logged in')


class CustomLogout(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
