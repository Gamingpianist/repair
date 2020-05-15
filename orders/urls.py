from django.urls import path

from .views import OrderView, OrderListView, search, OrdersubView

urlpatterns = [
    path('order/', OrderListView.as_view()),
    path('order-add/', OrderView.as_view()),
    path('search/', search),
    #path('order-detail/', viewID),
    path('order-detail/', OrdersubView.as_view())
]
