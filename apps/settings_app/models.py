from django.db import models

class ChurchSettings(models.Model):
    """Paramètres généraux de l'église (singleton)"""
    name        = models.CharField(max_length=255, default="Mon Église")
    tagline     = models.CharField(max_length=255, blank=True)
    email       = models.EmailField(blank=True)
    phone       = models.CharField(max_length=30, blank=True)
    address     = models.CharField(max_length=255, blank=True)
    facebook    = models.URLField(blank=True)
    youtube     = models.URLField(blank=True)
    instagram   = models.URLField(blank=True)
    whatsapp    = models.CharField(max_length=30, blank=True)
    logo        = models.ImageField(upload_to="settings/", null=True, blank=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paramètres de l'église"

    def __str__(self):
        return self.name

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
