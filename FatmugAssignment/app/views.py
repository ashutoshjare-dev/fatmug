from app.models import Vendor, PurchaseOrder
from app.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Vendor Profile Management
class VendorViewset(viewsets.ModelViewSet):
    """
    GET/List:
    returns list of vendors
    POST:
    creates a new vendor on POST request.
    GET/Retrive:
    returns a vendor with given id
    POST:
    updates a vendor with given id
    DELETE:
    deletes a vendor with given id
    """

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


# Purchase Order Tracking
class PurchaseOrderViewset(viewsets.ModelViewSet):
    """
    GET/List:
    returns all purchase orders
    POST:
    creates purchase order
    GET/Retrive:
    returns a purchase order with given id
    POST:
    updates a purchase order with given id
    DELETE:
    deletes a purchase order with given id
    """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class VendorPerformanceAPIView(APIView):
    """
    GET:
    returns performance of requested vendor
    """
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        vendor = get_object_or_404(Vendor, pk=pk)
        if vendor.performance:
            data = {
                "on_time_delivery_rate": vendor.performance.on_time_delivery_rate,
                "quality_rating_avg": vendor.performance.quality_rating_avg,
                "average_response_time": vendor.performance.average_response_time,
                "fulfillment_rate": vendor.performance.fulfillment_rate,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "No Data related to performance."},
                status=status.HTTP_400_BAD_REQUEST,
            )


# Purchase Order Acknowledgement
class AcknowledgePurchaseOrder(APIView):
    """
    POST
    updates acknowledgment_date of a vendor
    """
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)

        acknowledgment_date = request.data.get("acknowledgment_date", None)
        if not acknowledgment_date:
            return Response(
                {"error": "acknowledgment_date Not Provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Update acknowledgment date
        purchase_order.acknowledgment_date = acknowledgment_date
        purchase_order.save()

        # Serialize and return updated purchase order
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data, status=status.HTTP_200_OK)
