from django.urls import path
from .views import User_Login_TemplateView, User_Register_CreateView

urlpatterns = [
    path('user/login/', User_Login_TemplateView.as_view(), name='user_login'),
    path('user/register/', User_Register_CreateView.as_view(), name='user_register'),
    path('user/register/<int:referral_code>/', User_Register_CreateView.as_view(), name='user_register'),
    # path('user/logout'),

    # path('sub-admin/login/'),
    # path('sub-admin/logout/'),

    # path('password/reset/'),
    # path('password/reset/done/'),
    # path('password/reset/confirm/<uidb64>/<token>/'),
    # path('password/reset/complete/'),

]
