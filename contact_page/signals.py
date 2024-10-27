from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.signals import request_finished
from .models import HelpLine

@receiver(post_save, sender=HelpLine)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        print(f'New issue reported by {instance.name}: {instance.issue}')
