from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Donation
from .serializers import DonationSerializer, DonationUpdateSerializer
from apps.users.permissions import IsAdminOrStaff

class DonationListView(generics.ListAPIView):
    queryset           = Donation.objects.all()
    serializer_class   = DonationSerializer
    permission_classes = [IsAdminOrStaff]
    filter_backends    = [filters.SearchFilter]
    search_fields      = ["donor_name", "email", "phone"]

    def get_queryset(self):
        qs     = super().get_queryset()
        status = self.request.query_params.get("status")
        if status:
            qs = qs.filter(status=status)
        return qs

class DonationCreateView(generics.CreateAPIView):
    queryset           = Donation.objects.all()
    serializer_class   = DonationSerializer
    permission_classes = [AllowAny]

class DonationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Donation.objects.all()
    permission_classes = [IsAdminOrStaff]

    def get_serializer_class(self):
        if self.request.method in ("PATCH", "PUT"):
            return DonationUpdateSerializer
        return DonationSerializer
