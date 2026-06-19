from django.urls import path
from .views import TeachingListCreateView, TeachingDetailView

urlpatterns = [
    path("",          TeachingListCreateView.as_view()),
    path("<int:pk>/", TeachingDetailView.as_view()),
]
