from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = "main/mainpage.html"


class UsersView(TemplateView):
    template_name = 'main/users.html'


class CreateUsers(TemplateView):
    template_name = 'main/create_user.html'


class UserUpdate(TemplateView):
    template_name = 'main/update_user.html'


class Login(TemplateView):
    template_name = 'main/login_page.html'


class UserDelete(TemplateView):
    template_name = 'main/user_delete.html'
