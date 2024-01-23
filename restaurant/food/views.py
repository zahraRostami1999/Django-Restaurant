from django.shortcuts import render
from .models import Material

# Create your views here.

def material(request):
    materialItem = material.objects.all()
    return render(request, 'kitchen.html', {'materialItem': materialItem})