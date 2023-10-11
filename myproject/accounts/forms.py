from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class CustomUserForm(UserCreationForm):
#     phone_number = forms.CharField(max_length=15)
#     class Meta:
#         model = User
#         fields =['username','email','password1','password2','phonenumber']
        
        
        
class CustomUserForm(UserCreationForm):
    # phone_number = forms.CharField(max_length=15)  
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'enter a username '}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'enter email '}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'enter password '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'confirm password '}))
    phone_number = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'enter a phone number'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        
        # conditions for phn num validation
        if not phone_number.isdigit() or len(phone_number) < 10 or len(phone_number) > 13 :
            raise forms.ValidationError("invalid phone number.")
        return phone_number

    def clean_username(self):
        username = self.cleaned_data['username']
        if not len(username) > 4:
             raise forms.ValidationError("Given user name is short.")
        return username
            