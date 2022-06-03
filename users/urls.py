from django.urls import path, include

from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('users/', UserList.as_view(), name='users'),
]
