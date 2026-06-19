from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import EvangelisationRegistration
from .serializers import EvangelisationSerializer
from apps.users.permissions import IsAdminOrStaff

class EvangelisationCreateView(generics.CreateAPIView):
    queryset           = EvangelisationRegistration.objects.all()
    serializer_class   = EvangelisationSerializer
    permission_classes = [AllowAny]

class EvangelisationListView(generics.ListAPIView):
    queryset           = EvangelisationRegistration.objects.all()
    serializer_class   = EvangelisationSerializer
    permission_classes = [IsAdminOrStaff]
