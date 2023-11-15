from django.urls import path
from .views import *
from shop.views import IndexView



urlpatterns = [
    path ('signup', SignupView.as_view(),name = 'signup'),
    path ('login', LoginView.as_view(),name = 'login'),
    path ('logout', LogoutView.as_view(),name = 'logout'),
    path('otp-verification/<str:email>/', OTPVerificationView.as_view(), name='otp-verification'),
]