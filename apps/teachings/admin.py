from django.contrib import admin
from .models import Teaching

@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    list_display  = ["title", "speaker", "date", "category"]
    list_filter   = ["category"]
    search_fields = ["title", "speaker"]
