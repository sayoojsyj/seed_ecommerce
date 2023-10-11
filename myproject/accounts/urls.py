from django.urls import path
# from . import views
from .views import SignupView,LoginView,LogoutView


urlpatterns = [
    # path('',views.index,name='index'),
    path ('signup', SignupView.as_view(),name = 'signup'),
    path ('login', LoginView.as_view(),name = 'login'),
    path ('logout', LogoutView.as_view(),name = 'logout'),
]