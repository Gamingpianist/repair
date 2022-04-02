from django.urls import path

from .views import OrderView, OrderListView, search, OrdersubView, delete_order

urlpatterns = [
    path('order/', OrderListView),
    path('order-add/', OrderView.as_view()),
    path('search/', search),
    path('order-detail/', OrdersubView.as_view()),
    path('delete/', delete_order),
]
