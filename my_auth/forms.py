import random
import string
from django import forms
from .models import User, Referral
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def validate_image_size(image):
    max_size = 1 * 1024 * 1024 
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 1 MB.')

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
        max_length=80,
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Type your email'
        }),
    )
    country_code = forms.ChoiceField(
        label='Country Code',
        choices=User.COUNTRY_CODE_CHOICES,
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
        label='Referral Code',
        max_length=9,
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
            raise forms.ValidationError('This number already exists.')
        return number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")

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

        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()

            if referral_user:
                user.referraled_by = referral_user
                user.save()

                Referral.objects.create(referrer=referral_user, referred_user=user)

                referral_user.balance += Decimal(0.30)
                referral_user.save()

        return user

class UserLoginForm(forms.Form):
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
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': '********',
        }),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

class SubAdminLoginForm(forms.Form):
    ACCOUNT_TYPE_CHOICES = [
        ('senior_manager', 'Senior Manager'),
        ('manager', 'Manager'),

        ('senior_team_leader', 'Senior Team Leader'),
        ('team_leader', 'Team Leader'),

        ('trainer', 'Trainer'),

        ('senior_teacher', 'Senior Teacher'),
        ('teacher', 'Teacher'),

        ('accounter', 'Accounter'),

        ('help-line', 'Help-Line'),
    ]

    account_type = forms.ChoiceField(
        choices=ACCOUNT_TYPE_CHOICES,
        required=True
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
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': '********'}),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

class AnySubAdminCreateForm(forms.ModelForm):

    ACCOUNT_TYPE_CHOICES = [
        ('senior_manager', 'Senior Manager'),
        ('manager', 'Manager'),

        ('senior_team_leader', 'Senior Team Leader'),
        ('team_leader', 'Team Leader'),

        ('trainer', 'Trainer'),

        ('senior_teacher', 'Senior Teacher'),
        ('teacher', 'Teacher'),

        ('accounter', 'Accounter'),

        ('help-line', 'Help-Line'),
    ]

    COUNTRY_CODE_CHOICES = [
        ('Bangladesh', '+88'),
        ('India', '+91'),
    ]

    class Meta:
        model = User
        fields = ['image', 'email', 'country_code', 'number', 'password', 'first_name', 'last_name', 'address', 'city', 'state', 'country', 'account_type']

    def __init__(self, *args, **kwargs):
        super(AnySubAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['image'].validators = [validate_image_size]
        self.fields['country_code'].choices = self.COUNTRY_CODE_CHOICES
        self.fields['account_type'].choices = self.ACCOUNT_TYPE_CHOICES
        self.fields['password'].required = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    def save(self, commit=True):
        user = super(AnySubAdminCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.user_id = self._generate_user_id()
        user.role = 'sub_admin'
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user
    
    def _generate_user_id(self):
        return ''.join(random.choices(string.digits, k=9))

class TeamLeaderCreateForm(forms.ModelForm):
    COUNTRY_CODE_CHOICES = [
        ('Bangladesh', '+88'),
        ('India', '+91'),
    ]

    class Meta:
        model = User
        fields = ['image', 'email', 'country_code', 'number', 'password', 'first_name', 'last_name', 'address', 'city', 'state', 'country']

    def __init__(self, *args, **kwargs):
        super(TeamLeaderCreateForm, self).__init__(*args, **kwargs)
        self.fields['image'].validators = [validate_image_size]
        self.fields['country_code'].choices = self.COUNTRY_CODE_CHOICES
        self.fields['password'].required = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    def save(self, commit=True):
        user = super(TeamLeaderCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.user_id = self._generate_user_id()
        user.role = 'sub_admin'
        user.account_type = 'team_leader'
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user
    
    def _generate_user_id(self):
        return ''.join(random.choices(string.digits, k=9))

class TrainerCreateForm(forms.ModelForm):
    COUNTRY_CODE_CHOICES = [
        ('Bangladesh', '+88'),
        ('India', '+91'),
    ]

    class Meta:
        model = User
        fields = ['image', 'email', 'country_code', 'number', 'password', 'first_name', 'last_name', 'address', 'city', 'state', 'country']

    def __init__(self, *args, **kwargs):
        super(TrainerCreateForm, self).__init__(*args, **kwargs)
        self.fields['image'].validators = [validate_image_size]
        self.fields['country_code'].choices = self.COUNTRY_CODE_CHOICES
        self.fields['password'].required = True

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password

    def save(self, commit=True):
        user = super(TrainerCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.user_id = self._generate_user_id()
        user.role = 'sub_admin'
        user.account_type = 'trainer'
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user
    
    def _generate_user_id(self):
        return ''.join(random.choices(string.digits, k=9))





