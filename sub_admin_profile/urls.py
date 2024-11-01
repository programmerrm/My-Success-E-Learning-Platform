from django.urls import path
from .views import AllStudent, UpdatedProfile, ChangePassword

urlpatterns = [
    path('all-student/', AllStudent.as_view(), name='all_student'),
    path('profile/', UpdatedProfile.as_view(), name='sub_admin_profile'),
    path('change-password/', ChangePassword.as_view(), name='change_password'),
]
