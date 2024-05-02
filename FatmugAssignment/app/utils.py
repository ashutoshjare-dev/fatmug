from django.db.models import Avg
from django.utils import timezone
from .models import PurchaseOrder

# utils to calculate data for HistoricalPerformance instance
# all the utils require vendor instance as a parameter for calculations
def calculate_on_time_delivery_rate(vendor):
    """
    function to calculate percentage of on time deliveries.
    """
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status="completed")
    total_completed_orders = completed_orders.count()
    if total_completed_orders == 0:
        return 0.0

    on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now())
    total_on_time_orders = on_time_orders.count()

    return (total_on_time_orders / total_completed_orders) * 100


def calculate_quality_rating_avg(vendor):
    """
    function to calculate rating average.
    """
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status="completed"
    ).exclude(quality_rating=None)
    if not completed_orders:
        return 0.0

    avg_quality_rating = completed_orders.aggregate(Avg("quality_rating"))[
        "quality_rating__avg"
    ]
    return avg_quality_rating


def calculate_average_response_time(vendor):
    """
    function to calculate average response time.
    """
    completed_orders = PurchaseOrder.objects.filter(
        vendor=vendor, status="completed", acknowledgment_date__isnull=False
    )
    if not completed_orders:
        return 0.0

    total_response_time = sum(
        (order.acknowledgment_date - order.issue_date).total_seconds()
        for order in completed_orders
    )
    total_orders = completed_orders.count()

    return total_response_time / total_orders


def calculate_fulfillment_rate(vendor):
    """
    function to calculate fulfillment rate of a vendor.
    """
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    if total_orders == 0:
        return 0.0

    successful_orders = PurchaseOrder.objects.filter(vendor=vendor, status="completed")
    if successful_orders == 0:
        return 0.0

    successful_orders_count = successful_orders.count()

    return (successful_orders_count / total_orders) * 100
