from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ups/', views.ups, name='ups'),
    path('contact/', views.contact, name='contact'),
    path('footer-contact/', views.footer_contact, name='footer_contact'),
]