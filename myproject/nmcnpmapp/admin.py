# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_approved')  # Đảm bảo 'is_approved' được hiển thị trong danh sách
    list_filter = ('is_approved',)  # Thêm bộ lọc cho 'is_approved'
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_approved',)}),  # Thêm 'is_approved' vào trang sửa thông tin người dùng
    )

admin.site.register(CustomUser, CustomUserAdmin)
