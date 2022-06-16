from django.urls import path
from .views  import *

urlpatterns = [
    path('', TaskPage.as_view(), name='tasks'),
    path('create/', AddTask.as_view(), name='add_t'),
    path('<int:task_id>', TaskDescription.as_view(), name='desc'),
    path('/(?P<pk>\d+)/$/update', TaskUpdate.as_view(), name='task_update'),
    path('/(?P<pk>\d+)/$/delete', TaskDelete.as_view(), name='task_delete')
]