from django.urls import path
from .views  import *

urlpatterns = [
    path('', LabelPage.as_view(), name='labels'),
    path('create/', AddLabel.as_view(), name='add_l'),
    path('(?P<pk>\d+)/$/update/', LabelUpdate.as_view(), name='label_update'),
    path('(?P<pk>\d+)/$/delete/', LabelDelete.as_view(), name='label_delete')
]