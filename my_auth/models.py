import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

def validate_image_size(image):
    max_size = 1 * 1024 * 1024 
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 1 MB.')

def convert_image_to_webp(image_field):
    image = Image.open(image_field)
    output_io_stream = BytesIO()
    
    image.save(output_io_stream, format='WebP', quality=85)
    output_io_stream.seek(0)
    converted_image = InMemoryUploadedFile(output_io_stream, 'ImageField', f"{os.path.splitext(image_field.name)[0]}.webp", 'image/webp', image.size, None)
    return converted_image

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
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

        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    USER_ROLES_CHOICES = [
        ('user', 'User'),
        ('sub_admin', 'Sub Admin'),
        ('admin', 'Admin'),
    ]
    COUNTRY_CODE_CHOICES = [
        ('Bangladesh', '+88'),
        ('India', '+91'),
    ]
    user_id = models.CharField(
        unique=True,
        max_length=9,
        verbose_name='User ID'
    )
    image = models.ImageField(
        validators=[validate_image_size],
        upload_to='images/',
        blank=True, 
        null=True, 
        verbose_name='User Image'
    )
    balance = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0.00, 
        verbose_name='Balance'
    )
    email = models.EmailField(
        unique=True, 
        max_length=80,
        verbose_name='Email',
    )
    country_code = models.CharField(
        max_length=20, 
        choices=COUNTRY_CODE_CHOICES, 
        default='Bangladesh'
    )
    number = models.CharField(
        max_length=11,
        unique=True, 
        verbose_name='Number'
    )
    first_name = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name='Last Name'
    )
    address = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='Address'
    )
    city = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name='City'
    )
    state = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name='State'
    )
    country = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Country Name'
    )
    bio = models.TextField(
        max_length=500, 
        blank=True, 
        null=True, 
        verbose_name='Bio'
    )
    account_type = models.CharField(
        max_length=20, 
        choices=ACCOUNT_TYPE_CHOICES, 
        default='user'
    )
    role = models.CharField(
        max_length=20, 
        choices=USER_ROLES_CHOICES, 
        default='user'
    )
    referraled_by = models.ForeignKey(
        'self', 
        related_name='referrals',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name='Referred By'
    )

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
        ordering = ['-date_joined']

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original_user = User.objects.get(pk=self.pk)
            if self.is_active and not original_user.is_active:
                if self.referraled_by:
                    referrer = self.referraled_by
                    referrer.balance += 150
                    referrer.save()
                else:
                    print('No referrer found for this user.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Referral(models.Model):
    referrer = models.ForeignKey(
        User, 
        related_name='referrals_sent', 
        on_delete=models.CASCADE
    )
    referred_user = models.ForeignKey(
        User, 
        related_name='referrals_received',
        on_delete=models.CASCADE
    )
    date_referred = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Referral'
        verbose_name_plural = 'Referral'
        ordering = ['-date_referred']

    def __str__(self):
        return f'{self.referrer.email} referred {self.referred_user.email}'
