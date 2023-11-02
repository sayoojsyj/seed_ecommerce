from django.shortcuts import render
from .models import *
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
        bnr_img = banner_images.objects.all()
        catgry = Category.objects.all()
        context = {
        'item' : items,
        'photos' : bnr_img,
        'Categories': catgry,
        }
        return render(request, 'index.html', context)
    
    
def current_user (request):
    user_name = CustomUser.objects.all()
    context = {'username' : user_name}
    return render ( 'index.html' , context )

def category (request):
    catgry= Category.objects.all()
    context = {
        'Categories': catgry,
        }
    return render (request, "Products/category.html",context)


