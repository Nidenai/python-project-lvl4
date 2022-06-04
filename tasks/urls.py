from django.urls import path
from .views  import *

urlpatterns = [
    path('', TaskPage.as_view(), name='tasks'),
    path('add_task/', AddTask.as_view(), name='add_t'),
    path('<int:task_id>', TaskDescription.as_view(), name='desc'),
    path('update/(?P<pk>\d+)/$', TaskUpdate.as_view(), name='task_update'),
    path('delete/(?P<pk>\d+)/$', TaskDelete.as_view(), name='task_delete')
]