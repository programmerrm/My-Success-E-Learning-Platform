from django.contrib import admin
from .models import ContactInfo, HelpLine

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['location', 'email', 'phone', 'google_map_url']

class HelpLineAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'issue']

admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(HelpLine, HelpLineAdmin)
