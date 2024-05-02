from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, HistoricalPerformance
from app.utils import *
from django.conf import settings
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=PurchaseOrder)
def update_historical_performance(sender, instance, **kwargs):
    """
    signal to update historical performance of vendor when Purchase Order is created or updated.
    """
    vendor = instance.vendor
    HistoricalPerformance.objects.update_or_create(
        vendor=vendor,
        defaults={
            "on_time_delivery_rate": calculate_on_time_delivery_rate(vendor),
            "quality_rating_avg": calculate_quality_rating_avg(vendor),
            "average_response_time": calculate_average_response_time(vendor),
            "fulfillment_rate": calculate_fulfillment_rate(vendor),
        },
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
