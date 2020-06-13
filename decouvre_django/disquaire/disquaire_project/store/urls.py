from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.listing),
    re_path(r'^(<album_id>[0-9]+)/$', views.detail),
]