import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

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

class Banner(models.Model):
    short_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Short Title',
    )
    title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        verbose_name='Banner Image',
        validators=[validate_image_size]
    )

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.image:
            self.image = convert_image_to_webp(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or "Untitled Banner"

class SpecialFeature(models.Model):
    icon = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        verbose_name='Feature Image',
        validators=[validate_image_size]
    )
    title = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='Title',
    )
    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Description',
    )

    class Meta:
        verbose_name = 'Special Feature'
        verbose_name_plural = 'Special Feature'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.icon:
            self.icon = convert_image_to_webp(self.icon)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or "Untitled Special Feature"  

class HelpLine(models.Model):
    telegram_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Telegram Url'
    )
    any_kind_of_problem_date = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Problem Solveing Date',
    )
    any_kind_of_problem_google_meeting_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Problem Solving Google Meet Url',
    )
    team_leader = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name='Team Teader Name',
    )
    team_leader_whatup_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name='Team Leader Whatsup Number',
    )
    trainer = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name='Trainer Name',
    )
    trainer_whatup_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name='Trainer Whatsup Number',
    )

    class Meta:
        verbose_name = 'Help Line'
        verbose_name_plural = 'Help Line'
        ordering = ['-id']

    def __str__(self):
        return self.team_leader

class LiveClass(models.Model):
    class_topic = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name='Class Topic',
    )
    joining_time = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='joining Time',
    )
    join_meeting_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Join Metting Url',
    )

    class Meta:
        verbose_name = 'Live Class'
        verbose_name_plural = 'Live Class'
        ordering = ['-id']

    def __str__(self):
        return self.class_topic

class AdminHelpLine(models.Model):
    number = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name='Admin Whatsup Number',
    )

    class Meta:
        verbose_name = 'Admin Help Line'
        verbose_name_plural = 'Admin Help Line'
        ordering = ['-id']

    def __str__(self):
        return self.number

class UserReview(models.Model):
    user = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE, 
        related_name='reviews', 
        verbose_name='Reviewed User'
    )
    title = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name='Review Title',
    )
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Review Description',
    )
    star = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name='Review Star',
    )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'
        ordering = ['-id']

    def __str__(self):
        return self.title or 'No Title'

class Achievement(models.Model):
    icon = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Achievement Icon',
        validators=[validate_image_size]
    )
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Title',
    )
    description = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='Description',
    )

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievement'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.icon:
            self.icon = convert_image_to_webp(self.icon)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
