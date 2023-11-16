from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from accounts.models import CustomUser
from django.views import View
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse
 
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
    


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            product_check = get_object_or_404(Products, products_id=prod_id)

            if cart.objects.filter(user=request.user.id, product_id=prod_id).exists():
                return JsonResponse({'status': 'Product already added in cart'})
            else:
                prod_qty = int(request.POST.get('product_qty'))
                if product_check.quantity >= prod_qty:
                    cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    return JsonResponse({'status': 'Product added successfully'})
                else:
                    return JsonResponse({'status': f'Only {product_check.quantity} quantity is available'})
        else:
            return JsonResponse({'status': "Login to continue"})

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('index.html'))



# 
# def CartView(request):
#     cart= cart.objects.filter(user=request.user)
#     context={'cart':cart}
#     return render(request, 'Products/cart.html', context)

# class CartView(View):
    
#     def get(self,request):
#         cart= cart.objects.filter(user=request.user)
#         context={'cart':cart}
#         return render(request, 'Products/cart.html', context)

class CartView(View):
    template_name = 'Products/cart.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cart_items = cart.objects.filter(user=request.user)
        else:
            cart_items = None
        context = {'cart': cart_items}
        return render(request, self.template_name, context)
        
    




