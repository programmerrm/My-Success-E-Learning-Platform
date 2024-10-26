from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class Custome_User_Profile_Info(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['address', 'city', 'state', 'country', 'bio']