from django.shortcuts import render
from .models import Products , banner_images
from accounts.models import CustomUser
from django.views import View
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# Create your views here.





@method_decorator(never_cache, name='dispatch')
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
       
        items = Products.objects.all()
    
        return render(request, 'index.html', {'item' : items})
    
    
def current_user (request):
    user_name = CustomUser.objects.all()
    context = {'username' : user_name}
    return render ( 'index.html' , context )

def index (request):
    items = Products.objects.all()
    
    return render(request, 'index.html', {'item' : items})

def banner (request):
    bnr_img = banner_images.objects.all()
    
    return render(request, 'index.html', {'photos' : bnr_img})

