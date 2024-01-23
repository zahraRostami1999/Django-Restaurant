from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('menu/', views.menu , name = 'menu'),
]
