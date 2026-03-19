from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name',
        'last_name', 'is_active', 'is_staff'
    )
    list_filter = ('is_active', 'is_staff', 'date_joined')
    actions = ['block_users', 'unblock_users']

    def block_users(self, request, queryset):
        queryset.update(is_active=False)
    block_users.short_description = "Заблокировать выбранных пользователей"

    def unblock_users(self, request, queryset):
        queryset.update(is_active=True)
    unblock_users.short_description = "Разблокировать выбранных пользователей"


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)