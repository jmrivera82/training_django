from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    list_display=('username','is_staff','is_active')
    fieldsets= UserAdmin.fieldsets + (
        ('Additional information',{'fields':('birthdate',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)