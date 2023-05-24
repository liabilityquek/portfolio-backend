from django.db import models

class Portfolio(models.Model):
    project_link = models.URLField(blank=True, null=True)
    project_demo_link = models.URLField(blank=True, null=True)
    project_title = models.CharField(max_length=100, blank=True, null=True)
    project_image = models.URLField(max_length=300, blank=True, null=True)
    project_tech_stack = models.CharField(max_length=500, blank=True, null=True)
    project_description = models.CharField(max_length=1000, blank=True, null=True)
    project_created_at = models.DateTimeField(auto_now_add=True, null=True)
    project_updated_at = models.DateTimeField(auto_now=True, null=True)
