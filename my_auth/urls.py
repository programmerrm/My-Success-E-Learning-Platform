from django.urls import path
from .views import UserLogin, UserRegister, SubAdminLogin, UserLogout, SubAdminLogout, PasswordReset, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete

urlpatterns = [
    path('user/login/', UserLogin.as_view(), name='user_login'),
    path('user/register/', UserRegister.as_view(), name='user_register'),
    path('user/register/<int:referral_code>/', UserRegister.as_view(), name='user_register'),
    path('user/logout/', UserLogout.as_view(), name='user_logout'),
    path('sub-admin/login/', SubAdminLogin.as_view(), name='sub_admin_login'),
    path('sub-admin/logout/', SubAdminLogout.as_view(), name='sub_admin_logout'),

    path('password/reset/', PasswordReset.as_view(), name='password_reset'),
    path('password/reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
]