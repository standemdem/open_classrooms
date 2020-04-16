from django.urls import path

from . import views

urlpatterns = [
    path('', views.listing),
    path(r'^(?P<album_id>[0-9]+)/', views.detail),
]