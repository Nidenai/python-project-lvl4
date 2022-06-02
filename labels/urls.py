from django.urls import path
from .views  import *

urlpatterns = [
    path('', LabelPage.as_view(), name='labels'),
    path('add_labes/', AddLabel.as_view(), name='add_l')
]