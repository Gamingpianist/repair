from django.urls import path
from .views import LoginView, RegisterView, UpdateView, user_logout, book1, book2, book3, book4, gallery, read1, read2, read3


urlpatterns = [
    path('signin/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='register'),
    path('userupdate/', UpdateView.as_view(), name='update'),
    path('logout/', user_logout, name='logout'),
    path('book1/', book1),
    path('book2/', book2),
    path('book3/', book3),
    path('book4/', book4),
    path('gallery/', gallery),
    path('read1/', read1),
    path('read2/', read2),
    path('read3/', read3),
]
