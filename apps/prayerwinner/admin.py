from django.contrib import admin
from .models import PrayerRequest

@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display  = ["prenom", "nom", "tel", "situation", "status", "created_at"]
    list_filter   = ["status"]
    search_fields = ["prenom", "nom", "tel"]
    list_editable = ["status"]
