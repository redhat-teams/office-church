from django.db import models

class CCMContent(models.Model):
    """Contenu de la page Ministère / CCM"""
    title       = models.CharField(max_length=255)
    subtitle    = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to="ccm/", null=True, blank=True)
    video_url   = models.URLField(blank=True)
    order       = models.PositiveIntegerField(default=0)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
