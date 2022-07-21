from django.urls import path

from .views import StatusPage, AddStatus, StatusUpdate, StatusDelete

app_name = 'statuses'
urlpatterns = [
    path('', StatusPage.as_view(), name='list'),
    path('create/', AddStatus.as_view(), name='create'),
    path('<int:pk>/update/', StatusUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', StatusDelete.as_view(), name='delete')
]
