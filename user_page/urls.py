from django.urls import path
from .views import (
    ProfileTemplateView,
    ReferralTemplateView,
    PassbookTemplateView,
    WithdrawalTemplateView,
    AddressTemplateView,
    ChangePasswordTemplateView,
)

urlpatterns = [
    path('profile/', ProfileTemplateView.as_view(), name='user_profile'),
    path('referral/', ReferralTemplateView.as_view(), name='user_referral'),
    path('passbook/', PassbookTemplateView.as_view(), name='user_passbook'),
    path('withdrawal/', WithdrawalTemplateView.as_view(), name='user_withdrawal'),
    path('address/', AddressTemplateView.as_view(), name='user_address'),
    path('change-password/', ChangePasswordTemplateView.as_view(), name='user_change_password'),
]