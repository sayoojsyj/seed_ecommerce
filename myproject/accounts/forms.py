from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


# class CustomUserForm(UserCreationForm):
#     phone_number = forms.CharField(max_length=15)
#     class Meta:
#         model = User
#         fields =['username','email','password1','password2','phonenumber']
        
        
        
class CustomUserForm(UserCreationForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter your name '}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email '}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter password '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm password '}))
    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter a phone number'}))
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2', 'phone']

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
        
    #     # conditions for phn num validation
    #     if not phone_number.isdigit() or len(phone_number) < 10 or len(phone_number) > 13 :
    #         raise forms.ValidationError("invalid phone number.")
    #     return phone_number

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 4:
            raise forms.ValidationError("Given user name is short.")
        return name
            