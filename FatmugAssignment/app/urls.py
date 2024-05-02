from django.urls import path, include
from app.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LoginView, LogoutView


router = DefaultRouter()
router.register(r"vendors", VendorViewset, basename="vendor")
router.register(r"purchase_orders", PurchaseOrderViewset, basename="purchase_order")

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='index.html', next_page=''), name='logout'),
    path("gettoken/", obtain_auth_token, name="gettoken"),
    path("api/", include(router.urls)),
    path(
        "api/vendors/<int:pk>/performance",
        VendorPerformanceAPIView.as_view(),
        name="vendor_performance",
    ),
    path(
        "api/purchase_orders/<int:po_id>/acknowledge/",
        AcknowledgePurchaseOrder.as_view(),
        name="acknowledge_purchase_order",
    ),
]
