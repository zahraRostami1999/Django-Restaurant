from django.shortcuts import render
from .models import Material

# Create your views here.

def materials(request):
    materialItem = Material.objects.all()
    return render(request, 'kitchen.html', {'materialItem': materialItem})