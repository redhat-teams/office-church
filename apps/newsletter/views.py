from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import NewsletterSubscriber
from .serializers import NewsletterSerializer

class NewsletterSubscribeView(generics.CreateAPIView):
    queryset           = NewsletterSubscriber.objects.all()
    serializer_class   = NewsletterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get("email", "").lower().strip()
        if NewsletterSubscriber.objects.filter(email=email).exists():
            return Response({"detail": "Déjà inscrit."}, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)
