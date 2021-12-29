from django.urls import path

from . import views

urlpatterns = [
    path('on_publish/', views.on_publish),
    path('on_publish_done/', views.on_publish_done),
]
