from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .apps.users.views import CustomLogin, CustomLogout
from .views import HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', CustomLogout.as_view(), name='logout'),
    path('users/', include('task_manager.apps.users.urls', namespace='users')),
    path('labels/', include('task_manager.apps.labels.urls',
                            namespace='labels')),
    path('tasks/', include('task_manager.apps.tasks.urls', namespace='tasks')),
    path('statuses/', include('task_manager.apps.statuses.urls',
                              namespace='statuses'))
]
