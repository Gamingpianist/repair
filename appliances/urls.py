from django.urls import path

from .views import ApplianceView





urlpatterns = [
    path('services/', ApplianceView.as_view())
]