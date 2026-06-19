from django.urls import path
from .views import CCMListCreateView, CCMDetailView

urlpatterns = [
    path("",          CCMListCreateView.as_view()),
    path("<int:pk>/", CCMDetailView.as_view()),
]
