from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ("member", "Membre"),
        ("staff",  "Staff"),
        ("admin",  "Administrateur"),
    ]
    role  = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
    phone = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username
