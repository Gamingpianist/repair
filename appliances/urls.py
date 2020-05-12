from django.urls import path

from .views import ApplianceListView, viewByID, searchByName


urlpatterns = [
    path('', ApplianceListView.as_view()),
    path('view/', viewByID),
    path('search/', searchByName),
]
