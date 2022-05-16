from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('create_user', views.CreateUsers.as_view(), name='create_user'),
    path('login', views.LoginView.as_view(), name='login'),
]