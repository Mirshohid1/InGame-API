from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from users.models import User, Role


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ('-created_at',)
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'roles')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    readonly_fields = ('last_login', 'created_at', 'updated_at')

    fieldsets = (
        (_('Basic information'), {
            'fields': ('email', 'password')
        }),
        (_('Personal data'), {
            'fields': ('first_name', 'last_name', 'phone')
        }),
        (_('Access rights and roles'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'roles', 'groups', 'user_permissions')
        }),
        (_('System fields'), {
            'fields': ('last_login', 'created_at', 'updated_at')
        }),
    )

    add_fieldsets = (
        (_('Creating a user'), {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'roles', 'is_active', 'is_staff'),
        }),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
