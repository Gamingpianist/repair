from django.urls import path

from .views import NoticeListView, NoticeView

urlpatterns = [
    path('', NoticeListView.as_view()),
    path('view', NoticeView.as_view()),
]
