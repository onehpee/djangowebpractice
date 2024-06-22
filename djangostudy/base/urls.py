from django.urls import path

from . import views

urlpatterns = [
     path('', views.home, name="home"),
     # pk is a dynamic value it stands for primary key
     path('room/<str:pk>', views.room, name="room"),
     
     path('create-room/', views.createRoom, name="create-room"),
     path('update-room/<str:pk>/', views.updateRoom, name="update-room"),

]
