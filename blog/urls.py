from django.urls import path

from blog import views


urlpatterns = [
    path('stories', views.Feed.as_view(), name='stories-page'),
    path(r'^stories/?P<slug>[\w]+])/$', views.Detail.as_view(), name='detail'),
]
