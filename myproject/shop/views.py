from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from accounts.models import CustomUser
from django.views import View
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.urls import reverse
 
# Create your views here.





@method_decorator(never_cache, name='dispatch')
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        items = Products.objects.all()
        bnr_img = banner_images.objects.all()
        catgry = Category.objects.all()
        
        CartProduct = cart.objects.filter(user=self.request.user.id)
        total_quantity = sum(items.product_qty for items in CartProduct)
        context = {
        'item' : items,
        'photos' : bnr_img,
        'Categories': catgry,
        'total_quantity': total_quantity,
        }
        return render(request, 'index.html', context)
    
    


#for allcategory page

class AllCategoryView(View):
    
    def get(self, request):
        catgry = Category.objects.all()
         #To show the quantity of cart items 
        CartProduct = cart.objects.filter(user=self.request.user.id)
        total_quantity = sum(items.product_qty for items in CartProduct)
        context = {
        'Categories': catgry,
        'total_quantity': total_quantity,
        }
        return render (request,'Products/category.html',context)

#for a perticular category listing page

class CategoryView(View):
     
    def get(self, request,id):
        category = Category.objects.get(Category_id=id)
        prdct = Products.objects.filter(Category_id=category)
        #To show the quantity of cart items 
        CartProduct = cart.objects.filter(user=self.request.user.id)
        total_quantity = sum(items.product_qty for items in CartProduct)
        context = {
            'Products': prdct,
            'total_quantity': total_quantity,
        }
        return render(request, "Products/product_view.html",context )
    
#for a perticuar single product display page

class ProductDetail(View):
    def get(self,request,id):
        product = get_object_or_404(Products, products_id=id)
        #To show the quantity of cart items 
        CartProduct = cart.objects.filter(user=self.request.user.id)
        total_quantity = sum(items.product_qty for items in CartProduct)
        context = {
            'product': product,
            'total_quantity': total_quantity,
        }
        return render(request, 'Products/product-single.html', context)
    


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            #Products model whose products_id matches the value stored in the prod_id variable.
            product_check = get_object_or_404(Products, products_id=prod_id)

            if cart.objects.filter(user=request.user.id, product_id=prod_id).exists():
                return JsonResponse({'status': 'Product already added in cart'})
            else:
                prod_qty = int(request.POST.get('product_qty')) 
                if product_check.quantity >= prod_qty: #req qty available or not checking
                    # creating a new entry in the cart model 
                    cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    return JsonResponse({'status': 'Product added successfully'})
                else:
                    return JsonResponse({'status': f'Only {product_check.quantity} quantity is available'})
        else:
            return JsonResponse({'status': "Login to continue"})

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('index.html'))
    # def get(self, request, *args, **kwargs):
    #     return redirect('index')
    
    
    
            







class CartView(View):
    template_name = 'Products/cart.html'

    def get(self, request, *args, **kwargs):
        cart_items = None  # Set a default value
        if request.user.is_authenticated:
            cart_items = cart.objects.filter(user=request.user)
            #To show the quantity of cart items 
            CartProduct = cart.objects.filter(user=self.request.user.id)
            total_quantity = sum(items.product_qty for items in CartProduct)
            context = {
                'cart': cart_items,
                'total_quantity': total_quantity,
                }
            return render(request, self.template_name, context)
        else:
            return redirect("login")
        

class UpdateCartView(View):
    def post(self, request , *args, **kwargs):
        prod_id =request.POST.get('product_id')
        
        if (cart.objects.filter(user=request.user, product_id=prod_id)).exists():
            prod_qty = int(request.POST.get('product_qty'))
            Cart = cart.objects.get(product_id=prod_id, user=request.user)
            Cart.product_qty = prod_qty
            Cart.save()
            return JsonResponse({'status': 'updated successfully'})


class DeleteCartItem(View):
    def post(self, request , *args, **kwargs):
        prod_id =request.POST.get('product_id')
        
        if (cart.objects.filter(user=request.user, product_id=prod_id)).exists():
            cartitem=cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
            return JsonResponse({'status': 'Deleted successfully'})

# def DeleteCartItem(request):
#     if request.method == 'POST':
#         prod_id =request.POST.get('product_id')
#         if (cart.objects.filter(user=request.user, product_id=prod_id)).exists():
#             cartitem=cart.objects.get(product_id=prod_id, user=request.user)
#             cartitem.delete()
#             return JsonResponse({'status': 'Deleted successfully'})
        
        










