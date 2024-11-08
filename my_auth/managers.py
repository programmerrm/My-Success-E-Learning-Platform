import random
import string
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def _generate_user_id(self):
        return ''.join(random.choices(string.digits, k=9))
    
    def create_user(self, email, number, password, **extra_fields):
        if not email:
            raise ValueError('Email must be required')
        if not number:
            raise ValueError('Number must be required')
            
        email = self.normalize_email(email)
        user_id = self._generate_user_id()
        extra_fields.setdefault('user_id', user_id)

        user = self.model(
            email=email,
            number=number,
            role='user',
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, number, password=None, **extra_fields):
        user = self.create_user(
            email=email,
            number=number,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.role = 'admin'
        user.account_type = 'admin'
        user.save(using=self._db)
        return user
    