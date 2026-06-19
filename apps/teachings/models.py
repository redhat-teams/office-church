from django.db import models

class Teaching(models.Model):
    CATEGORY_CHOICES = [
        ("enseignement",   "Enseignement"),
        ("predication",    "Prédication"),
        ("etude_biblique", "Étude biblique"),
        ("temoignage",     "Témoignage"),
        ("autre",          "Autre"),
    ]
    title       = models.CharField(max_length=255)
    speaker     = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    date        = models.DateField()
    category    = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="enseignement")
    video_url   = models.URLField(blank=True)
    audio_url   = models.URLField(blank=True)
    thumbnail   = models.ImageField(upload_to="teachings/", null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
