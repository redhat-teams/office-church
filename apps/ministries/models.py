from django.db import models

class Ministry(models.Model):
    name        = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to="ministries/", null=True, blank=True)
    leader      = models.CharField(max_length=150, blank=True)
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering  = ["order"]
        verbose_name_plural = "Ministries"

    def __str__(self):
        return self.name
