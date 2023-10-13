# from django.shortcuts import render,redirect
# from django.contrib import messages
# from .forms import CustomUserForm
# from django.contrib.auth import authenticate,login,logout
# # Create your views here.



# def index(request):
#     return render(request,'index.html')


# def signup (request):
#     if request.user.is_authenticated:
#         messages.warning(request,"You are logged in")
#         return redirect('/')
#     else:
#         form_details = CustomUserForm()
#         if request.method =='POST':
#             form_details = CustomUserForm(request.POST)
#             if form_details.is_valid():
#                 form_details.save()
#                 messages.success(request,"Registered succecfully")
#                 return redirect('login')
#         context = {'form' : form_details}
#         return render(request,"signup.html", context)





# def loginn(request):
#     if request.user.is_authenticated:
#         messages.warning(request,"You are logged in")
#         return redirect('/')
#     else:
#         if request.method == 'POST':
#             name = request.POST.get('username')
#             pswrd = request.POST.get('password')
            
#             user = authenticate(request, username=name, password=pswrd )
            
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "logged in succesfully")
#                 return redirect("/")
#             else:
#                 messages.success(request, "invalid credentials")
#                 return redirect('login')
#     return render(request, 'login.html')




# def logoutpage(request):
#     if request.user.is_authenticated:
#         logout(request)
#         messages.success(request, "loged out succesfully")
#         return redirect("/")





from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import CustomUserForm



class SignupView(View):
    template_name = 'signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, "You are logged in")
            return redirect('/')
        form_details = CustomUserForm()
        context = {'form': form_details}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated:
            messages.warning(request, "You are logged in")
            return redirect('/')
        form_details = CustomUserForm(request.POST)
        if form_details.is_valid():
            form_details.save()
            messages.success(request, "Registered successfully")
            return redirect('login')
        context = {'form': form_details}
        return render(request, self.template_name, context)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, "You are logged in")
            return redirect('/')
        return render(request, self.template_name)

    def post(self, request):
        if request.user.is_authenticated:
            messages.warning(request, "You are logged in")
            return redirect('/')
        # name = request.POST.get('username')
        email = request.POST.get('email')
        pswrd = request.POST.get('password')
        user = authenticate(request, email=email, password=pswrd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logged out successfully")
        return redirect('/')
    
    

