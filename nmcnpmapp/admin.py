# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_approved', 'name','dongphi','donggop')
    list_filter = ('group','is_approved','dongphi','donggop')  
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_approved','dongphi', 'donggop')}),  
    )


admin.site.register(CustomUser, CustomUserAdmin)

from django.shortcuts import render
from django.contrib.auth.models import Group

def service_view(request):
    user = request.user
    family_group = Group.objects.get(name='Tên group của bạn') 
    is_member = family_group.user_set.filter(id=user.id).exists()

    return render(request, 'service.html', {'is_member': is_member})
