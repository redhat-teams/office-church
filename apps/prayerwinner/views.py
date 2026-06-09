from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import PrayerRequest
from .serializers import PrayerRequestSerializer


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