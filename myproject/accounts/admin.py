from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'is_staff', 'is_active', 'phone')
    readonly_fields=('name', 'email', 'phone')


admin.site.register(CustomUser,UserAdmin)