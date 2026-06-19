from django.urls import path
from .views import DonationListView, DonationCreateView, DonationDetailView

urlpatterns = [
    path("",          DonationListView.as_view()),
    path("create/",   DonationCreateView.as_view()),
    path("<int:pk>/", DonationDetailView.as_view()),
]
