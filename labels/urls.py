from django.urls import path
from .views  import *

urlpatterns = [
    path('', LabelPage.as_view(), name='labels'),
    path('add_labes/', AddLabel.as_view(), name='add_l'),
    path('update/(?P<pk>\d+)/$', LabelUpdate.as_view(), name='label_update'),
    path('delete/(?P<pk>\d+)/$', LabelDelete.as_view(), name='label_delete')
]