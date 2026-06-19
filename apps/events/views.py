from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Event
from .serializers import EventSerializer
from apps.users.permissions import IsAdminOrStaff

class EventListCreateView(generics.ListCreateAPIView):
    queryset         = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields    = ["title", "description", "location", "category"]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrStaff()]
        return [AllowAny()]

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Event.objects.all()
    serializer_class   = EventSerializer
    permission_classes = [IsAdminOrStaff]
