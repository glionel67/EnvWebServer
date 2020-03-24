from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('EnvData/display', views.display, name='display'),
    path('EnvData/display/<str:duration>/', views.display, name='display'),
]