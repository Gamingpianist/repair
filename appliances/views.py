import json

from django.shortcuts import render
from django.views.generic.base import View

from .models import Appliance

# Create your views here.


class ApplianceView(View):

    def get(self, request):
        appliances = Appliance.objects.all()
        return render(request, "", {"appliances": appliances})
