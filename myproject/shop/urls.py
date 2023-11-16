from django.urls import path
from .views import *
from .import views





urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('categories/', AllCategoryView.as_view(), name='categories'),
    path('categories/<uuid:id>/', CategoryView.as_view(), name='category_products'),
    path('product/<uuid:id>/', views.ProductDetail.as_view(), name='product_detail'),
    
    path('add-to-cart', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', CartView.as_view(),name='cart')
    # path('cart',views.CartView,name='cart')
    
]