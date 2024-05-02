from django.db import models
from django.utils import timezone
import uuid


def generate_unique_id():
    return uuid.uuid4().hex


class Vendor(models.Model):
    """
    Model to store vendor details
    """
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, default=generate_unique_id, unique=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    """
    Model to store Purchase order details
    """

    # options for status field
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
    ]

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name} - {self.status}"


class HistoricalPerformance(models.Model):
    """
    Modal to store performance of a vendor
    """

    # added a reverse relation to avoid redundant fields in vendor modal
    vendor = models.OneToOneField(
        Vendor, on_delete=models.CASCADE, related_name="performance"
    )
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
