from django.urls import path
from .views  import *

urlpatterns = [
    path('', StatusPage.as_view(), name='statuses'),
    path('add_status/', AddStatus.as_view(), name='add_s'),
    path('update/(?P<pk>\d+)/$', StatusUpdate.as_view(), name='status_update'),
    path('delete/(?P<pk>\d+)/$', StatusDelete.as_view(), name='status_delete')
]