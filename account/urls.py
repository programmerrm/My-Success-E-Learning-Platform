from django.urls import path
from .views import IndexView

urlpatterns = [
    path('user/login/', IndexView.as_view(), name='account'),
    path('user/logout'),
    path('user/register/'),

    path('sub-admin/login/'),
    path('sub-admin/logout/'),

    path('password/reset/'),
    path('password/reset/done/'),
    path('password/reset/confirm/<uidb64>/<token>/'),
    path('password/reset/complete/'),

]
