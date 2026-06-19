from rest_framework import serializers
from .models import CCMContent

class CCMContentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CCMContent
        fields = "__all__"
