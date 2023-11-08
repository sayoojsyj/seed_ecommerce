
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import CustomUserForm
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

# from accounts.models import CustomUser
# from shop.views import items
# from shop.models import Products


# @method_decorator(never_cache, name='dispatch')
# class IndexView(View):
#     template_name = 'index.html'

#     def get(self, request):
#         # context = {'item' : items}
        
#         # return render(request, self.template_name,context)
#         items = Products.objects.all()
    
#         return render(request, 'index.html', {'item' : items})
    
    
# def current_user (request):
#     user_name = CustomUser.objects.all()
#     context = {'username' : user_name}
#     return render ( 'index.html' , context )


@method_decorator(never_cache, name='dispatch')
class SignupView(View):
    template_name = 'signup.html'

     
    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, "You are logged in")
            return redirect('index')
        form_details = CustomUserForm()
        context = {'form': form_details}
        return render(request, self.template_name, context)
    
    
    def post(self, request):
      
        form_details = CustomUserForm(request.POST)
        if form_details.is_valid():
            form_details.save()
            messages.success(request, "Registered successfully")
            return redirect('login')
        messages.error(request, "Registration failed")
        return render(request, self.template_name, {'form': form_details})

    
@method_decorator(cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True), name='dispatch')
 
# @method_decorator(never_cache, name='dispatch')
class LoginView(View):
    template_name = 'login.html'


    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, "You are logged in")
            return redirect('index')
        return render(request, self.template_name)

    def post(self, request):
        # if request.user.is_authenticated:
        #     messages.warning(request, "You are logged in")
        #     return redirect('/')
        # name = request.POST.get('username')
        email = request.POST.get('email')
        pswrd = request.POST.get('password')
        user = authenticate(request, email=email, password=pswrd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logged out successfully")
        return redirect('index')
    
    

