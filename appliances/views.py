import json

from django.shortcuts import render
from django.views.generic.base import View

from .models import Appliance

# Create your views here.


class ApplianceView(View):

    def get(self, request):
        appliances = Appliance.objects.all()
        return render(request, 'index.html', {"appliances": appliances})

    # def post(self, request):
    #     '''创建'''
    #     request_body = json.loads(request.body)['data']
    #     name = request_body['name']
    #     desc = request_body['desc']
    #     image = request_body['desc']

    #     Appliance.objects.create(name=name, description=desc, image=image)

    #     return render(request, "")
