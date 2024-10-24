from django.contrib import admin
from .models import Login_Register_Side_Bar

# Register your models here.

class LoginRegisterSideBarAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo', 'banner']

admin.site.register(Login_Register_Side_Bar, LoginRegisterSideBarAdmin)
