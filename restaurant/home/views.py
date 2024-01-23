from django.shortcuts import render, redirect
from .models import Menu

# Create your views here.

def home(request):
    owner = { 
        'name' : 'zahra',
        'lastName' : 'rostami'
    }
    return render(request, 'home.html', owner)

def menu(request):
    MenuItems = Menu.objects.all()
    return render(request, 'menu.html', {'menuItems': MenuItems})

def false_food_state(request, food_id):
    menu = Menu.objects.get(pk = food_id)
    menu.state = False
    menu.save()
    return redirect('menu')

def true_food_state(request, food_id):
    menu = Menu.objects.get(pk = food_id)
    menu.state = True
    menu.save()
    return redirect('menu')