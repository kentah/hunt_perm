from django.urls import path

from blog import views


urlpatterns = [
    path('stories', views.Feed.as_view(), name='stories-page'),
    path('stories/create', views.CreatePostView.as_view(), name='create-post'),
    path('stories/update', views.UpdatePostView.as_view(), name='update-post'),
    #path(r'^stories/?P<slug>[\w]+])/$', views.Detail.as_view(), name='detail'),
]
