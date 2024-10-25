from django.db import models
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 2 MB')

class Category(models.Model):

    name = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(
        max_length=80,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    image = models.ImageField(
        upload_to='blogs/',
        validators=[validate_image_size],
        default='images/default-avatar.png',
        blank=False,
        null=False,
    )

    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    short_title = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    short_description = models.TextField(
        max_length=300,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
