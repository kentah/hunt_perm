from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import View, TemplateView, ListView

from .models import Services, Histories


class Splash(TemplateView):

    template_name = '../templates/main/index.html'

    def getSplash(self, request, *args, **kwargs):
        response = HttpResponse
        return response

class Services(ListView):

    # will not use model, hard-code services
    model = Services
    template_name = '../templates/main/services.html'

    # will not use model, hard-code services
    def getServices(self, request, *args, **kwargs):

        data = Services.objects.all()

        return render(request, template_name, {'services': data})

class Histories(ListView):
    # past clients etc
    model = Histories
    template_name = '../templates/main/histories.html'


    def getHistories(self, request, *args, **kwargs):

        data = Histories.objects.all()

        return render(request, template_name, {'history': data})
