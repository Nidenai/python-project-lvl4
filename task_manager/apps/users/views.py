from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from task_manager.mixins import HandleNoPermissionMixin
from task_manager.apps.users.forms import UserCreationForm
from task_manager.apps.users.models import User


class Register(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    success_message = _('User register successful')


class UserList(ListView):
    queryset = User.objects.order_by('id')
    template_name = 'users/list.html'
    context_object_name = 'users'


class UserUpdate(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView): # noqa
    template_name = 'update.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = _('User changed successfully')
    restriction_message = \
        _('У вас нет прав для изменения другого пользователя')
    redirect_url_while_restricted = reverse_lazy('users:users')

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, _('User changed successfully'))
        return redirect('users:users')


class UserDelete(LoginRequiredMixin, HandleNoPermissionMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView): # noqa
    template_name = 'delete.html'
    model = User
    success_url = reverse_lazy('users:users')
    success_message = _('User deleted successfully')
    restriction_message = \
        _('У вас нет прав для изменения другого пользователя')
    redirect_url_while_restricted = reverse_lazy('users:users')

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
