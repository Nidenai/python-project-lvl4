from django.urls import path

from .views import TaskPage, AddTask, \
    TaskDescription, TaskUpdate, TaskDelete

app_name = 'tasks'
urlpatterns = [
    path('', TaskPage.as_view(), name='list'),
    path('create/', AddTask.as_view(), name='create'),
    path('<int:task_id>', TaskDescription.as_view(), name='detail'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='delete')
]
