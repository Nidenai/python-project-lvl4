"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import HomepageView
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('labels/', LabelPage.as_view(), name='labels'),
    path('tasks/', TaskPage.as_view(), name='tasks'),
    path('add_task/', AddTask.as_view(), name='add_t'),
    path('add_label/', AddLabel.as_view(), name='add_l'),
]
