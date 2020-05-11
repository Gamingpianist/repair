from django.urls import path
from .views import LoginView, RegisterView, userLogout, book1, book2, book3, book4


urlpatterns = [
    path('signin/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='register'),
    path('logout/', userLogout, name='logout'),
    path('book1/', book1),
    path('book2/', book2),
    path('book3/', book3),
    path('book4/', book4),
]