from django.contrib import admin
from .models import User, Referral

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'number', 'first_name', 'num_referrals', 'is_active', 'date_joined']
    search_fields = ['user_id', 'email', 'number']
    list_per_page = 20

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('referrals_sent')
        return queryset

    def num_referrals(self, obj):
        return obj.referrals_sent.count()

    num_referrals.short_description = 'Referrals Count'

admin.site.register(User, UserAdmin)

class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referrer', 'referred_user', 'date_referred']
    search_fields = ['referrer__email', 'referred_user__email']
    list_filter = ['date_referred']
    list_per_page = 10

admin.site.register(Referral, ReferralAdmin)
