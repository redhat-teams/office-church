from django.db import models

class Donation(models.Model):
    STATUS_CHOICES = [
        ("pending",   "En attente"),
        ("completed", "Validé"),
        ("failed",    "Échoué"),
        ("refunded",  "Remboursé"),
    ]
    METHOD_CHOICES = [
        ("wave",         "Wave"),
        ("orange_money", "Orange Money"),
        ("cinetpay",     "CinetPay"),
        ("paypal",       "PayPal"),
        ("cash",         "Espèces"),
        ("other",        "Autre"),
    ]
    donor_name     = models.CharField(max_length=150, blank=True)
    email          = models.EmailField(blank=True)
    phone          = models.CharField(max_length=30, blank=True)
    amount         = models.DecimalField(max_digits=12, decimal_places=2)
    currency       = models.CharField(max_length=10, default="FCFA")
    payment_method = models.CharField(max_length=20, choices=METHOD_CHOICES, default="wave")
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    message        = models.TextField(blank=True)
    transaction_id = models.CharField(max_length=150, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.donor_name or 'Anonyme'} — {self.amount} {self.currency}"
