from django.urls import path, include

from .views import Register, UserPage

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('user/', UserPage.as_view(), name='user'),
]
