from django.urls import path
from . import views

#define url pattern
urlpatterns = [
    path('', views.home,name='home'),
    path('contact/', views.contact_view,name='contact'),
    path('sucsess/', views.contact_sucsess, name='contact-sucsess'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('resister/', views.resister_view , name='resister'),
    path('protected/',views.ProtectedView.as_view , name='protected'),
]
