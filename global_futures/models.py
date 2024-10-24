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
