from django.urls import path
from .views import IndexView
from .import views



urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('category',views.category,name='category'),
    # path('product',views.ProductView,name='product_item'),
    path('product_item/<str:category_name>/', views.ProductView, name='ProductView'),
]