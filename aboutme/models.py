from django.db import models

class Profile(models.Model):
    greeting = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True,null=True)
    par_inro = models.TextField(blank=True, null=True)
    avatar_img = models.URLField(blank=True, null=True)
    cv_link = models.URLField(blank=True, null=True)
