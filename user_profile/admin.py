from django.contrib import admin
from .models import WithdrawalMethod, WithdrawalProcess

class WithdrawalMethodAdmin(admin.ModelAdmin):
    list_display = ['name']

class WithdrawalProcessAdmin(admin.ModelAdmin):
    list_display = ['method', 'number', 'amount', 'status', 'transaction_id']

admin.site.register(WithdrawalMethod, WithdrawalMethodAdmin)
admin.site.register(WithdrawalProcess, WithdrawalProcessAdmin)
