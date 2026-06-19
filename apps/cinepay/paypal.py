# apps/cinepay/paypal.py
import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

def get_paypal_token():
    response = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        auth=HTTPBasicAuth(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET),
        data={"grant_type": "client_credentials"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["access_token"]
