from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from phonenumber_field.modelfields import PhoneNumberField



class CustomUser(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  email = models.EmailField(unique=True)
  name=models.CharField(max_length=200 , null=True)
  is_active = models.BooleanField('access',default=True)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True) 
  phone = PhoneNumberField()
  


  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name','phone']

  def __str__(self):
    return self.name




