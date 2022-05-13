from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('register_place/', views.register_place, name='register_place'),
    path('map/', views.map, name='map')
]
