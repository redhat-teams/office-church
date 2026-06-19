from django.urls import path
from .views import EvangelisationCreateView, EvangelisationListView

urlpatterns = [
    path("",      EvangelisationCreateView.as_view()),
    path("list/", EvangelisationListView.as_view()),
]
