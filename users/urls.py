from django.urls import path, include

from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('users/', UserList.as_view(), name='users'),
    path('update/(?P<pk>\d+)/$', UserUpdate.as_view(), name='user_update'),
    path('delete/(?P<pk>\d+)/$', UserDelete.as_view(), name='user_delete')
]
