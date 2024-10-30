from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator

def validate_image_size(image):
    max_size = 2 * 1024 * 1024  # 2 MB
    if image.size > max_size:
        raise ValidationError('The image file size must be less than 2 MB.')

class Banner_Section(models.Model):

    short_title = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
    )

class Special_Fuature(models.Model):

    image = models.ImageField(
        upload_to='images/',
        validators=[validate_image_size],
        blank=True,
        null=True,
    )

    title = models.CharField(
        max_length=35,
        blank=True,
        null=True,
    )

    short_description = models.TextField(
        validators=[MaxLengthValidator(250)],
        blank=True,
        null=True,
    )

class Live_Class(models.Model):

    class_topic = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    joining_time = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    join_meeting_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

class Help_Line(models.Model):

    telegram_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    any_kind_of_problem_date = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    any_kind_of_problem_google_meeting_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    
    team_leader = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    team_leader_whatup_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    trainer = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    trainer_whatup_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

