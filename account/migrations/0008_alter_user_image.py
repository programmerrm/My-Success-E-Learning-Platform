# Generated by Django 5.1.2 on 2024-11-02 06:18

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_address_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[account.models.validate_image_size]),
        ),
    ]