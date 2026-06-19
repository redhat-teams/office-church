from rest_framework import serializers
from .models import Teaching

class TeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Teaching
        fields = "__all__"
