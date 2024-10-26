# Generated by Django 5.1.2 on 2024-10-26 10:53

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='images/default-avatar.png', null=True, upload_to='images/', validators=[account.models.validate_image_size]),
        ),
    ]
