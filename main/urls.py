from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('json/',views.json_upload, name ="jsonupld"),
     path('json/sample',views.getJsonSample, name ="jsonupld"),
]