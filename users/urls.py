from django.urls import path, include

from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('user/', UserPage.as_view(), name='user'),
    path('users/', UsersPage.as_view(), name='users')
]
