from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ("culte",          "Culte"),
        ("conference",     "Conférence"),
        ("formation",      "Formation"),
        ("evangelisation", "Évangélisation"),
        ("jeunesse",       "Jeunesse"),
        ("priere",         "Prière"),
        ("autre",          "Autre"),
    ]
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date        = models.DateField()
    time        = models.TimeField(null=True, blank=True)
    location    = models.CharField(max_length=255, blank=True)
    category    = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="culte")
    image       = models.ImageField(upload_to="events/", null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title
