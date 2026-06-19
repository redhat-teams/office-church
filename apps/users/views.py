from django.contrib.auth import get_user_model
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .permissions import IsAdminOrStaff

User = get_user_model()

# ── Profil de l'utilisateur connecté ──────────────────────────────────────────
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    return Response(UserSerializer(request.user).data)

# ── Liste paginée + recherche + création (admin) ──────────────────────────────
class UserListView(generics.ListCreateAPIView):
    queryset           = User.objects.all()
    permission_classes = [IsAdminOrStaff]
    filter_backends    = [filters.SearchFilter]
    search_fields       = ["username", "email", "first_name", "last_name"]

    def get_queryset(self):
        qs   = super().get_queryset()
        role = self.request.query_params.get("role")
        if role:
            qs = qs.filter(role=role)
        return qs

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserCreateSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # On renvoie l'utilisateur avec le serializer d'affichage (sans le mot de passe)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

# ── Détail / modification / suppression ───────────────────────────────────────
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset           = User.objects.all()
    permission_classes = [IsAdminOrStaff]

    def get_serializer_class(self):
        if self.request.method in ("PATCH", "PUT"):
            return UserUpdateSerializer
        return UserSerializer
