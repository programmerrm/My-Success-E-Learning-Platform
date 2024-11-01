from django.urls import path
from .views import User_Login_TemplateView, User_Register_CreateView, Sub_Admin_Login_TemplateView, User_Logout_View, Sub_Admin_Logout_View, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    path('user/login/', User_Login_TemplateView.as_view(), name='user_login'),
    path('user/register/', User_Register_CreateView.as_view(), name='user_register'),
    path('user/register/<int:referral_code>/', User_Register_CreateView.as_view(), name='user_register'),
    path('user/logout/', User_Logout_View.as_view(), name='user_logout'),

    path('sub-admin/login/', Sub_Admin_Login_TemplateView.as_view(), name='sub_admin_login'),
    path('sub-admin/logout/', Sub_Admin_Logout_View.as_view(), name='sub_admin_logout'),

    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
