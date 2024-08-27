# staff/admin.py
from django.contrib import admin
from .models import Staff

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain_of_study', 'years_of_experience', 'current_project')
    search_fields = ('name', 'domain_of_study')
    list_filter = ('domain_of_study', 'years_of_experience', 'current_project')
