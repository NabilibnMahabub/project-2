from django.urls import path
from . import views

#define url pattern
urlpatterns = [
    path('', views.index),
    path('contact/', views.contact_view,name='contact'),
    path('sucsess/',views.contact_sucsess,name='contact-sucsess')
]
