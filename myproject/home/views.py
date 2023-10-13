from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser

# Create your views here.



# def index(request):
#     return render(request,'index.html')


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
    
def current_user (request):
    user_name = CustomUser.objects.all()
    context = {'username' : user_name}
    return render ( 'index.html' , context )
    
    