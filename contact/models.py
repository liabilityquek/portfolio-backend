from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    contact_created_at = models.DateTimeField(auto_now_add=True, null=True)
    contact_updated_at = models.DateTimeField(auto_now=True)
    
class SocialMediaLinks(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    link_created_at = models.DateTimeField(auto_now_add=True, null=True)
    link_updated_at = models.DateTimeField(auto_now=True)
