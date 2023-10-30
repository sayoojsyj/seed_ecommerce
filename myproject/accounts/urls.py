from django.urls import path
from .views import SignupView,LoginView,LogoutView
from shop.views import IndexView



urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path ('signup', SignupView.as_view(),name = 'signup'),
    path ('login', LoginView.as_view(),name = 'login'),
    path ('logout', LogoutView.as_view(),name = 'logout'),
]