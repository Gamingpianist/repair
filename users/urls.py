from django.urls import path
from .views import LoginView, RegisterView, UpdateView, user_logout, gallery

urlpatterns = [
    path('signin/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='register'),
    path('userupdate/', UpdateView.as_view(), name='update'),
    path('logout/', user_logout, name='logout'),
    path('gallery/', gallery)

]
