from django.db import models

class PrayerRequest(models.Model):

    STATUS_CHOICES = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("rejected", "refused"),
    )

    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    ville = models.CharField(max_length=100, blank=True)

    situation = models.CharField(max_length=100)

    priere = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"