# apps/cinepay/cinetpay.py
import requests
from django.conf import settings

def create_cinetpay_payment(payload):
    response = requests.post(
        "https://api-checkout.cinetpay.com/v2/payment",
        json=payload,
        timeout=30,
    )
    return response.json()
