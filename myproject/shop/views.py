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
    print(catgry)
    context = {
        'Categories': catgry,
        }
    return render (request, "Products/category.html",context)
# def ProductView(request):
#     prdct= Products.objects.all()
#     context = {
#         'ProductDdetail' : prdct
#     }
#     return render (request, "Products/product_view.html",context)


# def ProductView(request,category_name):
#     # if (Category.objects.filter(name=category_name, status=0)):
#     if Category.objects.filter(name=category_name, status=0).exists():
#         # prdct= Products.objects.filter(Category_id=category)
#         prdct = Products.objects.filter(Category_id__name=category_name)
#         context = {
#             'ProductDdetail' : prdct
#         }
#         return render (request, "Products/product_view.html",context)
def ProductView(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        prdct = Products.objects.filter(Category_id=category)

        context = {
            'ProductDdetail': prdct,
            'category_name': category_name,
        }
        return render(request, "Products/product_view.html", context)
    except Category.DoesNotExist:
        return render(request, "category_not_found.html")



