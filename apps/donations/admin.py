from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display  = ["donor_name", "amount", "currency", "payment_method", "status", "created_at"]
    list_filter   = ["status", "payment_method"]
    search_fields = ["donor_name", "email", "phone"]
