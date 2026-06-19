from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import PrayerRequest
from .serializers import PrayerRequestSerializer
from apps.users.permissions import IsAdminOrStaff


class PrayerRequestListView(generics.ListAPIView):
    """Liste des demandes de prière — réservé au staff/admin."""
    queryset = PrayerRequest.objects.all().order_by("-created_at")
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminOrStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ["prenom", "nom", "tel", "ville"]


class PrayerRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Détail / mise à jour du statut / suppression — réservé au staff/admin."""
    queryset = PrayerRequest.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminOrStaff]


class PrayerRequestCreateView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = PrayerRequestSerializer(
            data=request.data
        )

        if serializer.is_valid():

            obj = serializer.save()

            return Response({
                "id": obj.id,
                "status": obj.status
            })

        return Response(
            serializer.errors,
            status=400
        )
    

class PrayerRequestStatusView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, pk):

        try:
            prayer = PrayerRequest.objects.get(pk=pk)

            return Response({
                "id": prayer.id,
                "status": prayer.status
            })

        except PrayerRequest.DoesNotExist:

            return Response(
                {"error": "Demande introuvable"},
                status=404
            )