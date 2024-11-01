from django.contrib import admin
from .models import Login_Register_Side_Bar, LogoImage, FooterLogo, SocialMediaIcon, ContactInfoFooter, FooterCopyRightText, FooterPaymentMethodImage

# Register your models here.

class LoginRegisterSideBarAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo', 'banner']

class LogoImageAdmin(admin.ModelAdmin):
    list_display = ['image']


admin.site.register(Login_Register_Side_Bar, LoginRegisterSideBarAdmin)
admin.site.register(LogoImage, LogoImageAdmin)
admin.site.register(FooterLogo)
admin.site.register(SocialMediaIcon)
admin.site.register(ContactInfoFooter)
admin.site.register(FooterCopyRightText)
admin.site.register(FooterPaymentMethodImage)
