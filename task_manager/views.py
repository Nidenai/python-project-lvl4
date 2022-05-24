from django.views.generic import TemplateView
from django.shortcuts import render


class HomepageView(TemplateView):
    template_name = 'home.html'

    def check_user(self, request):
        if user == 'AnonymousUser':
            context = 'Приветствуем, Гость! Хотите зарегистрироваться?'
        else:
            context = f'Приветствую, {user}'
        return render(request, self.template_name, context)
