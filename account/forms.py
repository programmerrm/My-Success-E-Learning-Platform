from django import forms
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()

class User_Register_Form(forms.ModelForm):

    email = forms.EmailField(
        label='Email',
        min_length=8,
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Type your email'
        }),
    )

    country_code = forms.ChoiceField(
        label='Country Code',
        choices=User.COUNTRY_CODE,
        required=True,
    )

    number = forms.CharField(
        label='WhatsApp Number',
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'WhatsApp number',
        }),
    )

    first_name = forms.CharField(
        label='First Name',
        min_length=3,
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name'
        }),
    )

    last_name = forms.CharField(
        label='Last Name',
        min_length=3,
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name'
        }),
    )

    password = forms.CharField(
        label='Password',
        min_length=5,
        max_length=15,
        widget=forms.PasswordInput(attrs={
            'placeholder': '********',
        }),
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        min_length=5,
        max_length=15,
        widget=forms.PasswordInput(attrs={
            'placeholder': '********',
        }),
    )

    referral_code = forms.CharField(
        label='Referral code',
        min_length=6,
        max_length=6,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Referral code'}),
    )

    terms_agreement = forms.BooleanField(
        label='I agree to the Terms of Use and Privacy Policy',
        initial=True,
        required=True,
        error_messages={'required': 'You must agree to the terms.'}
    )

    class Meta:
        model = User
        fields = (
            'email',
            'country_code',
            'number',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'referral_code',
            'terms_agreement',
        )

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if User.objects.filter(number__iexact=number).exists():
            raise forms.ValidationError('This number already exists')
        return number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email already exists')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
    def clean_referral_code(self):
        code = self.cleaned_data.get('referral_code')
        if code:
            try:
                referral_user = User.objects.get(user_id=code)
                return referral_user
            except User.DoesNotExist:
                raise forms.ValidationError('Invalid referral code')
        return None

    def save(self, commit=True):
        user = super().save(commit=False)
        referral_user = self.cleaned_data.get('referral_code')
        if referral_user:
            user.referred_by = referral_user
            referral_user.balance += Decimal(0.30)
            referral_user.save()
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user

class User_Login_Form(forms.ModelForm):
    
    number = forms.CharField(
        label='WhatsApp Number',
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'WhatsApp number',
        }),
    )

    email = forms.EmailField(
        label='Email',
        min_length=8,
        max_length=50,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Type your email'
        }),
    )
