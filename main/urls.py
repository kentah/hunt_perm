from django.urls import path

from main import views


urlpatterns = [
    path('', views.Splash.as_view(), name='splash-page'),
    path('services', views.Services.as_view(), name='services-page'),
    path('histories', views.Histories.as_view(), name='histories-page'),
]
