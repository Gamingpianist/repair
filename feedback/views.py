from django.shortcuts import render
from django.views.generic.base import View

from .models import FeedBack
# Create your views here.


class FeedBackView(View):

    def get(self, request):
        feed_back = FeedBack.objects.all()
        return render(request, '', {'FeedBack': feed_back})
