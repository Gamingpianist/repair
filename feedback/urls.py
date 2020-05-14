from django.urls import path

from .views import FeedBackListView

urlpatterns = [
    path('', FeedBackListView.as_view()),
]
