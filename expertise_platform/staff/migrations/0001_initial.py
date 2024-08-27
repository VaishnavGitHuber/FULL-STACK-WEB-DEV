# Generated by Django 4.2.15 on 2024-08-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("domain_of_study", models.CharField(max_length=255)),
                ("years_of_experience", models.IntegerField()),
                ("contact_details", models.CharField(max_length=255)),
                ("certifications", models.JSONField()),
                (
                    "current_project",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
    ]
