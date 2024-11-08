import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

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

class Favicon(models.Model):
    icon = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        validators=[validate_image_size],
        verbose_name='Favicon Image'
    )

    class Meta:
        verbose_name = 'Favicon'
        verbose_name_plural = 'Favicon'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.icon:
            self.icon = convert_image_to_webp(self.icon)
        super().save(*args, **kwargs)

class Logo(models.Model):
    logo = models.ImageField(
        validators=[validate_image_size],
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Logo Image',
    )

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.logo:
            self.logo = convert_image_to_webp(self.logo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.logo.name

class LoginRegisterSideBar(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Title',
    )
    banner = models.ImageField(
        validators=[validate_image_size],
        upload_to='images',
        blank=True,
        null=True,
        verbose_name='banner Iamge',
    )
    
    class Meta:
        verbose_name = 'Login Register Side Bar'
        verbose_name_plural = 'Login Register Side Bar'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.banner:
            self.banner = convert_image_to_webp(self.banner)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
       
class FooterDescription(models.Model):
    short_description = models.TextField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Short Description',
    )

    class Meta:
        verbose_name = 'Footer Description'
        verbose_name_plural = 'Footer Description '
        ordering = ['-id']

    def __str__(self):
        return self.short_description

class SocialMediaIcon(models.Model):
    icon = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
        verbose_name='Social Media Icon',
    )
    url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Url Link',
    )

    class Meta:
        verbose_name = 'Social Media Icon'
        verbose_name_plural = 'Social Media Icon'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.icon:
            self.icon = convert_image_to_webp(self.icon)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url or "Social Media Icon"

class ContactInfoFooter(models.Model):
    address = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Address',
    )
    phone_number = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Phone Number',
    )
    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Email',
    )

    class Meta:
        verbose_name = 'Contact Info Footer'
        verbose_name_plural = 'Contact Info Footer'
        ordering = ['-id']

    def __str__(self):
        return self.email

class FooterCopyRightText(models.Model):
    text = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Footer Copy Right Text'
    )

    class Meta:
        verbose_name = 'Footer Copy Right Text'
        verbose_name_plural = 'Footer Copy Right Text'
        ordering = ['-id']

    def __str__(self):
        return self.text

class FooterPaymentMethodImage(models.Model):
    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
        verbose_name='Footer Payment Method Image',
    )

    class Meta:
        verbose_name = 'Footer Payment Method Image'
        verbose_name_plural = 'Footer Payment Method Image'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_image_to_webp(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment Method Image"    
