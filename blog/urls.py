from django.urls import path

from blog import views


urlpatterns = [
    path('stories', views.Feed.as_view(), name='stories-page'),
    #path('<int:post_id>/', views.full, name='full'),
]
