from django.db import models

class Testimonial(models.Model):
    name       = models.CharField(max_length=150)
    text       = models.TextField()
    image      = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    order      = models.PositiveIntegerField(default=0)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.name
