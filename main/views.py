from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from .models import Services, Histories


class Splash(TemplateView):

    template_name = '../templates/main/index.html'

    def getSplash(self, request, *args, **kwargs):
        response = HttpResponse
        return response

class Services(TemplateView):

    template_name = '../templates/main/services.html'
    data = Services.objects.all()

    def getServices(self, request, *args, **kwargs):
        response = HttpResponse
        return response

class Histories(TemplateView):

    template_name = '../templates/main/histories.html'

    data = Histories.objects.all()

    his = {'history': data}

    def getHistories(self, request, *args, **kwargs):
    #    response = HttpResponse
    #    return response
        return render(request, template_name, {'data': data})
