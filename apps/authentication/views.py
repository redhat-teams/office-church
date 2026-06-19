from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from apps.users.permissions import IsAdminOrStaff

@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    return Response({"status": "ok"})

@api_view(["GET"])
@permission_classes([IsAdminOrStaff])
def admin_stats(request):
    """Statistiques pour le tableau de bord admin"""
    from apps.events.models import Event
    from apps.teachings.models import Teaching
    from apps.donations.models import Donation

    User = get_user_model()

    donations_qs = Donation.objects.all()
    total_amount = sum(d.amount for d in donations_qs)

    import datetime
    today = datetime.date.today()

    upcoming_events = Event.objects.filter(date__gte=today).order_by("date")[:5]
    recent_donations = Donation.objects.order_by("-created_at")[:5]

    from apps.events.serializers import EventSerializer
    from apps.donations.serializers import DonationSerializer

    return Response({
        "users_count":     User.objects.count(),
        "events_count":    Event.objects.count(),
        "teachings_count": Teaching.objects.count(),
        "donations_count": Donation.objects.count(),
        "donations_total": float(total_amount),
        "upcoming_events":   EventSerializer(upcoming_events, many=True, context={"request": request}).data,
        "recent_donations":  DonationSerializer(recent_donations, many=True, context={"request": request}).data,
    })
