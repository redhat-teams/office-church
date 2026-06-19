from django.db import models

class EvangelisationRegistration(models.Model):
    """Inscription au programme d'évangélisation"""
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(blank=True)
    phone      = models.CharField(max_length=30)
    city       = models.CharField(max_length=100, blank=True)
    message    = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
