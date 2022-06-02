from django.urls import path
from .views  import *

urlpatterns = [
    path('', StatusPage.as_view(), name='statuses'),
    path('add_status/', AddStatus.as_view(), name='add_s')
]