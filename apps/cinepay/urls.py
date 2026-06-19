from django.urls import path
from .views import create_cinetpay_checkout, cinetpay_webhook

urlpatterns = [
    path("cinetpay/create/",  create_cinetpay_checkout),
    path("cinetpay/webhook/", cinetpay_webhook),
]
