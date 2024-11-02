from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from .managers import UserManager
from decimal import Decimal

def validate_image_size(image):
    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 2 MB')

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    ACCOUNT_TYPE = [
        ('STL', 'Senior Team Leader'),
        ('TL', 'Team Leader'),
        ('STEAM', 'Selling Team'),
        ('MT', 'Marketing Team'),
        ('QT', 'Qualification Team'),

        ('HL', 'Help-Line'),
        ('TR', 'Trainer'),

        ('ST', 'Senior Teacher'),
        ('TEACHER', 'Teacher'),
        ('PET', 'Photo Editing Teacher'),
        ('VET', 'Video Editing Teacher'),
        ('SMT', 'Social Marketing Teacher'),

        ('COUNSELLOR', 'Counsellor'),
        ('SC', 'Senior Counsellor'),

        ('SM', 'Senior Manager'),
        ('CM', 'Counsellor Manager'),
        ('MM', 'Marketing Manager'),
        ('ACCOUNTER', 'Accounter'),

        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    ]

    USER_ROLES = [
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
        ('SUB_ADMIN', 'Sub Admin'),
    ]

    COUNTRY_CODE = [
        ('BD', '+88'),
        ('IND', '+91'),
    ]

    user_id = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        default=0.00,
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
    )

    country_code = models.CharField(
        max_length=10,
        choices=COUNTRY_CODE,
        default='+88',
    )

    number = models.CharField(
        max_length=11,
        unique=True,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    city = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    state = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    country = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    bio = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    referred_by = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='referrals'
    )

    account_type = models.CharField(
        max_length=50,
        choices=ACCOUNT_TYPE,
        default='USER',
    )

    role = models.CharField(
        max_length=20,
        choices=USER_ROLES,
        default='USER',
    )

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    has_received_bonus = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.number
    
    def add_bonus(self):
        if self.account_type == 'STL':
            self.balance += Decimal(50.00)
        elif self.account_type == 'TL':
            self.balance += Decimal(30.00)
        elif self.account_type == 'TR':
            self.balance += Decimal(10.00)
        self.save()

    @classmethod
    def distribute_bonuses(cls):
        for user in cls.objects.filter(is_staff=True):
            if not user.has_received_bonus:
                user.add_bonus()
                user.has_received_bonus = True
                user.save()

def promote_user_to_admin(user):
    user.is_staff = True
    user.add_bonus()
    user.save()