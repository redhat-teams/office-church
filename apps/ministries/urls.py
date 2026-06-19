from django.urls import path
from .views import MinistryListCreateView, MinistryDetailView

urlpatterns = [
    path("",          MinistryListCreateView.as_view()),
    path("<int:pk>/", MinistryDetailView.as_view()),
]
