from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('EnvData/display', views.display, name='display'),
    path('EnvData/display/<str:duration>/', views.display, name='display'),
    path('EnvData/realtime', views.realtime, name='realtime'),
    path('EnvData/realtime/update', views.update, name='update'),
    #path('EnvData/temperature', views.temperature, name='temperature'),
    #path('EnvData/humidity', views.humidity, name='humidity'),
    #path('EnvData/pressure', views.pressure, name='pressure'),
]