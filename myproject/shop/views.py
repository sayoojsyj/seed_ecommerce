from django.shortcuts import render,get_object_or_404
from .models import *
from accounts.models import CustomUser
from django.views import View
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
 
# Create your views here.





@method_decorator(never_cache, name='dispatch')
class IndexView(View):
    template_name = 'index.html'

#for index page
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
    
    
# def current_user (request):
#     user_name = CustomUser.objects.all()
#     context = {'username' : user_name}
#     return render ( 'index.html' , context )

#for allcategory page

class AllCategoryView(View):
    
    def get(self, request):
        catgry= Category.objects.all()
        context = {
        'Categories': catgry,
        }
        return render (request,'Products/category.html',context)

#for a perticular category listing page

class CategoryView(View):
     
    def get(self, request,id):
        category = Category.objects.get(Category_id=id)
        prdct = Products.objects.filter(Category_id=category)
        context = {
            'Products': prdct,
        }
        return render(request, "Products/product_view.html",context )
    
#for a perticuar single product display page

class ProductDetail(View):
    def get(self,request,id):
        product = get_object_or_404(Products, products_id=id)
        context = {
             'product': product
        }
        return render(request, 'Products/product-single.html', context)
    



