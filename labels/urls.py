from django.urls import path

from .views import *

app_name = 'labels'
urlpatterns = [
    path('', LabelPage.as_view(), name='list'),
    path('create/', AddLabel.as_view(), name='create'),
    path('<int:pk>/update/', LabelUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', LabelDelete.as_view(), name='delete')
]
