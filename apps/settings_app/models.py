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

    # ── Événement majeur (section countdown affichée sur l'accueil) ──────────
    major_event_enabled     = models.BooleanField(default=True)
    major_event_badge       = models.CharField(max_length=100, blank=True, default="Évènement Majeur - Église")
    major_event_title       = models.CharField(max_length=255, blank=True, default="Conférence Internationale du Réveil 2026")
    major_event_description = models.TextField(blank=True, default="Rejoignez-nous pour un moment exceptionnel de réveil spirituel, de prière, d'adoration et d'enseignement.")
    major_event_date        = models.DateTimeField(null=True, blank=True)
    major_event_location    = models.CharField(max_length=255, blank=True, default="Salle de conférence de l'église")
    major_event_cta_label   = models.CharField(max_length=100, blank=True, default="Rejoindre maintenant")
    major_event_cta_link    = models.CharField(max_length=255, blank=True, default="/contact")

    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paramètres de l'église"

    def __str__(self):
        return self.name

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
