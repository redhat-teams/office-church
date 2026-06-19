from django.contrib import admin
from .models import EvangelisationRegistration

@admin.register(EvangelisationRegistration)
class EvangelisationAdmin(admin.ModelAdmin):
    list_display  = ["first_name", "last_name", "phone", "city", "created_at"]
    search_fields = ["first_name", "last_name", "phone"]
