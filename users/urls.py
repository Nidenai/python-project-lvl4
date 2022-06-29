from django.urls import path, include

from .views import *

urlpatterns = [
    path('create/', Register.as_view(), name='register'),
    path('', UserList.as_view(), name='users'),
    path('/(?P<pk>\d+)/$/update', UserUpdate.as_view(), name='user_update'),
    path('/(?P<pk>\d+)/$/delete', UserDelete.as_view(), name='user_delete')
]
