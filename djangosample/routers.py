from rest_framework import routers
from invoice.viewsets import InvoiceViewSet

router = routers.DefaultRouter()

router.register(r'invoice', InvoiceViewSet)