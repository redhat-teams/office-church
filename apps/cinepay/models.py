# apps/payments/models.py

from django.db import models

class Payment(models.Model):

    PROVIDERS = (
        ("cinetpay", "CinetPay"),
        ("paypal", "PayPal"),
    )

    STATUS = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    )

    transaction_id = models.CharField(max_length=150, unique=True)

    provider = models.CharField(
        max_length=20,
        choices=PROVIDERS
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    customer_email = models.EmailField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id