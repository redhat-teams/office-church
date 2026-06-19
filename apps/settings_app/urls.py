from django.urls import path
from .views import ChurchSettingsView

urlpatterns = [
    path("", ChurchSettingsView.as_view()),
]
