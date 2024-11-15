from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.index_title = 'DASHBOARD'

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_admin', 'is_staff', 'is_pelanggan')
    list_filter = ('is_staff', 'is_pelanggan')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_admin', 'is_staff', 'is_pelanggan')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_pelanggan'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, UserAdmin)
