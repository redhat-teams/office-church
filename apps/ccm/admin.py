from django.contrib import admin
from .models import CCMContent

@admin.register(CCMContent)
class CCMAdmin(admin.ModelAdmin):
    list_display = ["title", "order", "is_active"]
    list_filter  = ["is_active"]
