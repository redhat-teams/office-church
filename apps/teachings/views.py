from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Teaching
from .serializers import TeachingSerializer
from apps.users.permissions import IsAdminOrStaff

class TeachingListCreateView(generics.ListCreateAPIView):
    queryset         = Teaching.objects.all()
    serializer_class = TeachingSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields    = ["title", "speaker", "description", "category"]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrStaff()]
        return [AllowAny()]

class TeachingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Teaching.objects.all()
    serializer_class   = TeachingSerializer
    permission_classes = [IsAdminOrStaff]
