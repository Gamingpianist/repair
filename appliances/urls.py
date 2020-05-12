from django.urls import path
from django.conf.urls import url
from .views import ApplianceListView, viewByID, searchByName


urlpatterns = [
    path('services/', ApplianceListView.as_view()),
    path('service-detail/', viewByID),
    path('search/', searchByName),
]

