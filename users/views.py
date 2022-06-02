from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from users.forms import UserCreationForm, UserList


class Register(View):
    template_name = 'registration/register.html'

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


class UserPage(TemplateView):
    template_name = 'user.html'


class UsersPage(TemplateView):
    template_name = 'users.html'

    def get(self, request):
        users = UserList.objects.all()
        context = {
            'users': users
        }
        return render(request, self.template_name, context)
