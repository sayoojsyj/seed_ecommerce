from django.urls import path
from accounts.views import IndexView



urlpatterns = [
    path('', IndexView.as_view(),name='index'),
   
]