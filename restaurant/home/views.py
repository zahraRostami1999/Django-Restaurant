from django.shortcuts import render
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