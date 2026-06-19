from django.urls import path
from .views import (
    PrayerRequestCreateView,
    PrayerRequestStatusView,
    PrayerRequestListView,
    PrayerRequestDetailView,
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

    path(
        "list/",
        PrayerRequestListView.as_view(),
        name="prayer-request-list"
    ),

    path(
        "<int:pk>/",
        PrayerRequestDetailView.as_view(),
        name="prayer-request-detail"
    ),
]