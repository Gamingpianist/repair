from django.shortcuts import render
from django.views.generic.base import View

from .models import Order

# Create your views here.


class OrderListView(View):

    def get(self, request):

        orders = Order.objects.all()
        user = request.user
        return render(request, "index.html", {"orders": orders, "user": user})
