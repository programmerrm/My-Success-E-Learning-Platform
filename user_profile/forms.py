from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import WithdrawalProcess, WithdrawalMethod
from django.contrib.auth import get_user_model

User = get_user_model()

class WithdrawalRequestForm(forms.ModelForm):
    
    method = forms.ModelChoiceField(
        queryset=WithdrawalMethod.objects.all(),
        empty_label="Select a method",
        required=True,
    )

    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=500,
        required=True,
    )

    number = forms.CharField(
        max_length=100,
        required=True,
    )

    class Meta:
        model = WithdrawalProcess
        fields = ['method', 'amount', 'number']

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if not number:
            raise forms.ValidationError("This field is required")
        return number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['method'].queryset = WithdrawalMethod.objects.all()


class Custome_User_Profile_Info(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['address', 'city', 'state', 'country', 'bio']
    