from django.urls import path

from .views import NoticeListView, NoticeView

urlpatterns = [
    path('notice/', NoticeListView),
    path('notice-detail/', NoticeView.as_view()),
]
