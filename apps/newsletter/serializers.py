from rest_framework import serializers
from .models import NewsletterSubscriber

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = NewsletterSubscriber
        fields = ["id", "email", "created_at"]
