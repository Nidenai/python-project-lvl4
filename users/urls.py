from django.urls import path, include

from .views import *

app_name = 'users'
urlpatterns = [
    path('create/', Register.as_view(), name='register'),
    path('', UserList.as_view(), name='users'),
    path('<int:pk>/update/', UserUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', UserDelete.as_view(), name='delete')
]
