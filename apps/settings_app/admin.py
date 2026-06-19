from django.contrib import admin
from .models import ChurchSettings

@admin.register(ChurchSettings)
class ChurchSettingsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "updated_at"]
