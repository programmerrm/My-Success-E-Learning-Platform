from django.db import models
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 2 MB')

# Create your models here.

class Login_Register_Side_Bar(models.Model):
    logo = models.ImageField(
        upload_to='login-register-side-bar/',
        validators=[validate_image_size],
        default='images/logo.png',
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    banner = models.ImageField(
        upload_to='login-register-side-bar/',
        validators=[validate_image_size],
        default='images/about-page-defult-thumb.jpg',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Login/Register Sidebar'
        verbose_name_plural = 'Login/Register Sidebar'
        ordering = ['logo', 'title', 'banner']

    def __str__(self):
        return self.title

class LogoImage(models.Model):

    image = models.ImageField(
        upload_to='login-register-side-bar/',
        validators=[validate_image_size],
        default='images/logo.png',
        blank=True,
        null=True,
    )

class FooterLogo(models.Model):

    short_description = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.short_description

class SocialMediaIcon(models.Model):

    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
    )

    url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.url or "Social Media Icon"

class ContactInfoFooter(models.Model):

    address = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.email

class FooterCopyRightText(models.Model):

    text = models.TextField(
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text

class FooterPaymentMethodImage(models.Model):
    
    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Payment Method Image {self.id}"
    