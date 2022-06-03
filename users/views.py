from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView
from users.models import User
from users.forms import UserCreationForm


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



class UserList(ListView):
    queryset = User.objects.order_by('id')
    template_name = 'users.html'
    context_object_name = 'users'
