from django.urls import path

from .views import FeedBackListView, FeedView, searchfor, FeedbacksubView, delete_feedback

urlpatterns = [
    path('feedback/', FeedBackListView.as_view()),
    path('feedback-add/', FeedView.as_view()),
    path('searchfor/', searchfor),
    path('feedback-detail/', FeedbacksubView.as_view()),
    path('delete/', delete_feedback),
]
