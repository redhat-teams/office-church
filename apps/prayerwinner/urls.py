from django.urls import path
from .views import (
    PrayerRequestCreateView,
    PrayerRequestStatusView,
)

urlpatterns = [
    path(
        "",
        PrayerRequestCreateView.as_view(),
        name="prayer-request-create"
    ),

    path(
        "<int:pk>/status/",
        PrayerRequestStatusView.as_view(),
        name="prayer-request-status"
    ),
]