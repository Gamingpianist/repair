from django.urls import path
from .views import LoginView, RegisterView


urlpatterns = [
    path('signin/', LoginView.as_view()),
    path('signup/', RegisterView.as_view()),
]