from django.db import models

class ContactInfo(models.Model):
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True)
    google_map_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.email
    
class HelpLine(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    issue = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
