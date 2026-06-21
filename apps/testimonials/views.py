from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from .models import Testimonial
from .serializers import TestimonialSerializer
from apps.users.permissions import IsAdminOrStaff


class TestimonialListCreateView(generics.ListCreateAPIView):
    """
    Liste publique des témoignages actifs (utilisée sur la page d'accueil),
    et création réservée au staff/admin.
    """
    serializer_class = TestimonialSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields    = ["name", "text"]

    def get_queryset(self):
        qs = Testimonial.objects.all()
        # Le public ne voit que les témoignages actifs ; l'admin voit tout
        # quand il consulte la liste depuis /admin (paramètre explicite).
        if self.request.query_params.get("all") != "1":
            qs = qs.filter(is_active=True)
        return qs

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminOrStaff()]
        return [AllowAny()]


class TestimonialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Testimonial.objects.all()
    serializer_class   = TestimonialSerializer
    permission_classes = [IsAdminOrStaff]
