from django.urls import path
from .views import IndexView, User_Register_CreateView

urlpatterns = [
    path('user/login/', IndexView.as_view(), name='user_login'),
    # path('user/logout'),
    path('user/register/', User_Register_CreateView.as_view(), name='user_register'),

    # path('sub-admin/login/'),
    # path('sub-admin/logout/'),

    # path('password/reset/'),
    # path('password/reset/done/'),
    # path('password/reset/confirm/<uidb64>/<token>/'),
    # path('password/reset/complete/'),

]
