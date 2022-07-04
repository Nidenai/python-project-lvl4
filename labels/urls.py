from django.urls import path
from .views  import *

urlpatterns = [
    path('', LabelPage.as_view(), name='labels'),
    path('create/', AddLabel.as_view(), name='add_l'),
    path('<int:pk>/update/', LabelUpdate.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDelete.as_view(), name='label_delete')
]