from django.urls import path
from . import views

#define url pattern
urlpatterns = [
    path('', views.index)
]
