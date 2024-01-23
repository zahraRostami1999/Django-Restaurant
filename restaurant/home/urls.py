from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('menu/', views.menu , name = 'menu'),
    path('end/<int:food_id>/', views.false_food_state, name = 'end' ),
    path('add/<int:food_id>/', views.true_food_state , name = 'add'),
]
