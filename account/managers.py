from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, number, password, **extra_fields):

        if not email:
            raise ValueError('Email must be required')
        if not number:
            raise ValueError('Number must be required')
        
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            number=number,
            role='USER',
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, number, password, **extra_fields):
        
        user = self.create_user(
            email=email,
            number=number,
            password=password,
            **extra_fields,
        )
        
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.role = 'ADMIN'
        user.save(using=self._db)
        return user
    
    def create_sub_admin(self, email, number, password, **extra_fields):
        
        user = self.create_user(
            email=email,
            number=number,
            password=password,
            **extra_fields,
        )

        user.role = 'SUB_ADMIN'
        user.save(using=self._db)
        return user