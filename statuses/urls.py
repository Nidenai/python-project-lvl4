from django.urls import path
from .views  import *

urlpatterns = [
    path('', StatusPage.as_view(), name='statuses'),
    path('create/', AddStatus.as_view(), name='add_s'),
    path('<int:pk>/update/', StatusUpdate.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDelete.as_view(), name='status_delete')
]