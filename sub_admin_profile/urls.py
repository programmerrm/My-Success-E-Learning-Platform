from django.urls import path
from .views import AllStudent, UpdatedProfile, ChangePassword, Withdrawal, Passbook, PendingStudent

urlpatterns = [
    path('all-student/', AllStudent.as_view(), name='all_student'),
    path('pending-student', PendingStudent.as_view(), name='pending_student'),
    path('profile/', UpdatedProfile.as_view(), name='sub_admin_profile'),
    path('change-password/', ChangePassword.as_view(), name='change_password'),
    path('withdrawal/', Withdrawal.as_view(), name='sub_admin_withdrawal'),
    path('passbook/', Passbook.as_view(), name='sub_admin_passbook'),
]
