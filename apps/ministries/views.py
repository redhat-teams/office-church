from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Ministry
from .serializers import MinistrySerializer
from apps.users.permissions import IsAdminOrStaff

class MinistryListCreateView(generics.ListCreateAPIView):
    queryset         = Ministry.objects.filter(is_active=True)
    serializer_class = MinistrySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrStaff()]
        return [AllowAny()]

class MinistryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Ministry.objects.all()
    serializer_class   = MinistrySerializer
    permission_classes = [IsAdminOrStaff]
