from rest_framework import serializers
from .models import Vendor, PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    """
    model serializer to serialize and deserialize data
    """

    class Meta:
        model = Vendor
        fields = "__all__"


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """
    model serializer to serialize and deserialize data
    """

    class Meta:
        model = PurchaseOrder
        fields = "__all__"
