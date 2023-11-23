
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import CustomUserForm
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import *





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
    
            # Generate and send OTP
            user_email = form_details.cleaned_data['email']

            # Generate a 6-digit OTP
            generated_otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

            # Store OTP in session
            request.session['otp'] = generated_otp

            # Send OTP to email
            send_mail(
                'Your OTP for Signup',
                f'Your OTP is: {generated_otp}',
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False,
            )
            return redirect('otp-verification', email=user_email)
            
        else:
            messages.error(request, "Registration failed")
            return render(request, self.template_name, {'form': form_details})





class OTPVerificationView(View):
    template_name = 'otp_verification.html'

    def get(self, request, email):
        
        context = {'email': email}
        return render(request, self.template_name, context)

    def post(self, request, email):
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')  

        if entered_otp == stored_otp:
            messages.success(request, "Registered successfully")
            return redirect('login')
        else:
            print('Invalid OTP entered:', entered_otp)
            messages.error(request, "Invalid OTP")
            return redirect('otp-verification', email=email)


    

    
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
    
    

