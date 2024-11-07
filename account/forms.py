import random
from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from decimal import Decimal

def validate_image_size(image):
    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 2 MB')

User = get_user_model()

class TrainerCreateForm(forms.ModelForm):
    COUNTRY_CODE = [
        ('BD', '+88'),
        ('IND', '+91'),
    ]

    class Meta:
        model = User
        fields = ['image', 'email', 'country_code', 'number', 'password', 'first_name', 'last_name', 'address', 'city', 'state', 'country', 'bio']

    def __init__(self, *args, **kwargs):
        super(TrainerCreateForm, self).__init__(*args, **kwargs)
        self.fields['image'].validators = [validate_image_size]
        self.fields['country_code'].choices = self.COUNTRY_CODE
        self.fields['password'].required = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    def save(self, commit=True):
        user = super(TrainerCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.user_id = random.randint(100000, 999999)
        user.role = 'SUB_ADMIN'
        user.account_type = 'TR'
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user
    
class TeamLeaderCreateForm(forms.ModelForm):
    COUNTRY_CODE = [
        ('BD', '+88'),
        ('IND', '+91'),
    ]

    class Meta:
        model = User
        fields = ['image', 'email', 'country_code', 'number', 'password', 'first_name', 'last_name', 'address', 'city', 'state', 'country', 'bio']

    def __init__(self, *args, **kwargs):
        super(TeamLeaderCreateForm, self).__init__(*args, **kwargs)
        self.fields['image'].validators = [validate_image_size]
        self.fields['country_code'].choices = self.COUNTRY_CODE
        self.fields['password'].required = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    def save(self, commit=True):
        user = super(TeamLeaderCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.user_id = random.randint(100000, 999999)
        user.role = 'SUB_ADMIN'
        user.account_type = 'TL'
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user

class Sub_Admin_Login_Form(forms.Form):

    account_type = forms.ChoiceField(
        label='Account Type',
        choices=User.ACCOUNT_TYPE,
        required=True,
    )

    number = forms.CharField(
        label='WhatsApp Number',
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'WhatsApp number'}),
    )

    password = forms.CharField(
        label='Password',
        min_length=5,
        max_length=15,
        widget=forms.PasswordInput(attrs={'placeholder': '********'}),
    )

    class Meta:
        model = User
        fields = ['account_type', 'number', 'password',]

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

class User_Login_Form(forms.Form):

    number = forms.CharField(
        label='WhatsApp Number',
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'WhatsApp number',
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

    class Meta:
        model = User
        fields = ['number', 'password']

class ResetPasswordForm(SetPasswordForm):

    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}
        ),
        strip=False,
    )

    new_password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}
        ),
        strip=False,
    )

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        validate_password(password)
        return password
