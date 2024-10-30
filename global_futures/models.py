from django.db import models
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 2 MB')

# Create your models here.

class HeaderMenu(models.Model):

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

class Contact_Info(models.Model):

    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

class Footer_Bottom_Menu(models.Model):

    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    url = models.URLField(
        max_length=200,
        null=True,
        blank=True,
    )

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

class HeaderSection(models.Model):

    menu_list = models.ForeignKey(
        HeaderMenu,
        on_delete=models.CASCADE,
        related_name='header_section'
    )

class FooterSection(models.Model):

    contact_info = models.ForeignKey(
        Contact_Info,
        on_delete=models.CASCADE,
        related_name='contact_info',

    )

    payment_method_image = models.ImageField(
        validators=[validate_image_size],
        default='images/logo.png',
        blank=True,
        null=True,
    )

    copy_right_text = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    footer_bottom_menu_list = models.ForeignKey(
        Footer_Bottom_Menu,
        on_delete=models.CASCADE,
        related_name='footer_section',
    )
