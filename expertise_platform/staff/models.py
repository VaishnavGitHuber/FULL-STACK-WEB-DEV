# staff/models.py
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=255)
    domain_of_study = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    contact_details = models.CharField(max_length=255)
    # certifications = models.JSONField()  # Assuming certifications are stored as JSON
    current_project = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
