from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import ChurchSettings
from .serializers import ChurchSettingsSerializer
from apps.users.permissions import IsAdminOrStaff

class ChurchSettingsView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAdminOrStaff()]

    def get(self, request):
        settings = ChurchSettings.get_settings()
        return Response(ChurchSettingsSerializer(settings).data)

    def patch(self, request):
        settings   = ChurchSettings.get_settings()
        serializer = ChurchSettingsSerializer(settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
