from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView


class Splash(TemplateView):

    template_name = '../templates/main/index.html'

    def getSplash(self, request, *args, **kwargs):
        response = HttpResponse
        return response
