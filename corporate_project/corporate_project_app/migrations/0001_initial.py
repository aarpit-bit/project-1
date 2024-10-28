# Generated by Django 5.1.2 on 2024-10-28 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("description", models.TextField()),
                ("location", models.CharField(max_length=255)),
                ("industry", models.CharField(max_length=255)),
                ("website", models.URLField(max_length=255)),
                ("company_age", models.IntegerField()),
                ("company_net_worth", models.IntegerField()),
                ("company_founder", models.CharField(max_length=255)),
                ("company_headquarters", models.CharField(max_length=255)),
                ("company_ceo", models.CharField(max_length=255)),
                ("company_employees", models.IntegerField()),
                ("company_products", models.CharField(max_length=255)),
                ("company_services", models.CharField(max_length=255)),
                ("company_market_cap", models.IntegerField()),
                ("company_revenue", models.IntegerField()),
                ("company_profit", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("salary", models.IntegerField()),
                ("department", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("joining_date", models.DateField()),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("address", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="employee_images/"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employees",
                        to="corporate_project_app.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("budget", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "New"),
                            ("IN_PROGRESS", "In Progress"),
                            ("ON_HOLD", "On Hold"),
                            ("COMPLETED", "Completed"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="NEW",
                        max_length=20,
                    ),
                ),
                ("duration", models.IntegerField(help_text="Duration in days")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="corporate_project_app.company",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="corporate_project_app.employee",
                    ),
                ),
            ],
        ),
    ]