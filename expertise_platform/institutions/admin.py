# institutions/admin.py
from django.contrib import admin
from .models import Institution, Requirement

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_info')
    search_fields = ('name', 'location')

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ('institution', 'description', 'created_at')
    list_filter = ('institution',)
    search_fields = ('description',)
