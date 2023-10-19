from django.shortcuts import render
from .models import Products
# Create your views here.



def index (request):
    items = Products.objects.all()
    
    return render(request, 'index.html', {'item' : items})

