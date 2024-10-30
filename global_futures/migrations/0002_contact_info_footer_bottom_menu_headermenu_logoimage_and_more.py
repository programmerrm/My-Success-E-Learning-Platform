# Generated by Django 5.1.2 on 2024-10-29 09:19

import django.db.models.deletion
import global_futures.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_futures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer_Bottom_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='login-register-side-bar/', validators=[global_futures.models.validate_image_size])),
            ],
        ),
        migrations.CreateModel(
            name='FooterSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method_image', models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='', validators=[global_futures.models.validate_image_size])),
                ('copy_right_text', models.CharField(blank=True, max_length=150, null=True)),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to='global_futures.contact_info')),
                ('footer_bottom_menu_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_section', to='global_futures.footer_bottom_menu')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='header_section', to='global_futures.headermenu')),
            ],
        ),
    ]
