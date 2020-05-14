from django.urls import path

from .views import NoticeListView, NoticeView

urlpatterns = [
    path('notice/', NoticeListView.as_view()),
    path('notice-detail/', NoticeView.as_view()),
]
