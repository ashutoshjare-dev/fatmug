# Generated by Django 4.1.1 on 2024-05-01 16:13

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=100)),
                ("contact_details", models.TextField()),
                ("address", models.TextField()),
                (
                    "vendor_code",
                    models.CharField(
                        default=app.models.generate_unique_id,
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this vendor belongs to. A vendor will get all permissions granted to each of their groups.",
                        related_name="vendors",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vendor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this vendor.",
                        related_name="vendors",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
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
                ("po_number", models.CharField(max_length=100, unique=True)),
                ("order_date", models.DateTimeField()),
                ("delivery_date", models.DateTimeField()),
                ("items", models.JSONField()),
                ("quantity", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("completed", "Completed"),
                            ("canceled", "Canceled"),
                        ],
                        max_length=20,
                    ),
                ),
                ("quality_rating", models.FloatField(blank=True, null=True)),
                ("issue_date", models.DateTimeField(auto_now_add=True)),
                ("acknowledgment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.vendor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalPerformance",
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
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                ("on_time_delivery_rate", models.FloatField()),
                ("quality_rating_avg", models.FloatField()),
                ("average_response_time", models.FloatField()),
                ("fulfillment_rate", models.FloatField()),
                (
                    "vendor",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="performance",
                        to="app.vendor",
                    ),
                ),
            ],
        ),
    ]
