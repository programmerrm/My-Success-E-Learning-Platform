# Generated by Django 5.1.2 on 2024-10-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USER', 'User'), ('ADMIN', 'Admin'), ('SUB_ADMIN', 'Sub Admin')], default='USER', max_length=20),
        ),
    ]