from django.urls import path

from main import views


urlpatterns = [
    path('', views.Splash.as_view(), name='splash-page'),
]
