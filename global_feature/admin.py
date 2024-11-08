from django.contrib import admin
from .models import Favicon, Logo, LoginRegisterSideBar, FooterDescription, SocialMediaIcon, ContactInfoFooter, FooterCopyRightText, FooterPaymentMethodImage

# Register your models here.

admin.site.register(Favicon)
admin.site.register(Logo)
admin.site.register(LoginRegisterSideBar)
admin.site.register(FooterDescription)
admin.site.register(SocialMediaIcon)
admin.site.register(ContactInfoFooter)
admin.site.register(FooterCopyRightText)
admin.site.register(FooterPaymentMethodImage)
