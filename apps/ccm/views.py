from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CCMContent
from .serializers import CCMContentSerializer
from apps.users.permissions import IsAdminOrStaff

class CCMListCreateView(generics.ListCreateAPIView):
    queryset         = CCMContent.objects.filter(is_active=True)
    serializer_class = CCMContentSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrStaff()]
        return [AllowAny()]

class CCMDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = CCMContent.objects.all()
    serializer_class   = CCMContentSerializer
    permission_classes = [IsAdminOrStaff]
