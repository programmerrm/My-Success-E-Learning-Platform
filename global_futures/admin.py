from django.contrib import admin
from .models import Login_Register_Side_Bar, LogoImage, HeaderSection, FooterSection, HeaderMenu, Contact_Info, Footer_Bottom_Menu

# Register your models here.

class LoginRegisterSideBarAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo', 'banner']

class LogoImageAdmin(admin.ModelAdmin):
    list_display = ['image']

class HeaderMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']

class HeaderSectionAdmin(admin.ModelAdmin):
    list_display = ['menu_list']

class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ['contact_info', 'copy_right_text']

class Contact_Info_Admin(admin.ModelAdmin):
    list_display = ['name']

class Footer_Bottom_Menu_Admin(admin.ModelAdmin):
    list_display = ['name', 'url']

admin.site.register(Login_Register_Side_Bar, LoginRegisterSideBarAdmin)
admin.site.register(LogoImage, LogoImageAdmin)
admin.site.register(HeaderMenu, HeaderMenuAdmin)
admin.site.register(HeaderSection, HeaderSectionAdmin)
admin.site.register(FooterSection, FooterSectionAdmin)
admin.site.register(Contact_Info, Contact_Info_Admin)
admin.site.register(Footer_Bottom_Menu, Footer_Bottom_Menu_Admin)
