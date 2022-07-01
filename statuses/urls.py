from django.urls import path
from .views  import *

urlpatterns = [
    path('', StatusPage.as_view(), name='statuses'),
    path('create/', AddStatus.as_view(), name='add_s'),
    path('(?P<pk>\d+)/$/update/', StatusUpdate.as_view(), name='status_update'),
    path('(?P<pk>\d+)/$/delete/', StatusDelete.as_view(), name='status_delete')
]