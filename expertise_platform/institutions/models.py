# institutions/models.py
from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Requirement(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='requirements')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
