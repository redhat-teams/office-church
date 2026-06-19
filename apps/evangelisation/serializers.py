from rest_framework import serializers
from .models import EvangelisationRegistration

class EvangelisationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EvangelisationRegistration
        fields = "__all__"
