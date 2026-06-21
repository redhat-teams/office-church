from django.urls import path
from .views import TestimonialListCreateView, TestimonialDetailView

urlpatterns = [
    path("",          TestimonialListCreateView.as_view()),
    path("<int:pk>/", TestimonialDetailView.as_view()),
]
