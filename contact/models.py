from django.db import models
    
class SocialMediaLinks(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    link = models.CharField(blank=True, null=True, max_length=500)

