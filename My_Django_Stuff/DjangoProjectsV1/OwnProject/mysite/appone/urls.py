from django.urls import path, re_path
from appone import views

app_name = 'appone'

urlpatterns = [
    path('aboutme/', views.AboutMe, name='AboutMe'),
    path('contact/', views.Contact, name='Contact'),
    path('proone/', views.ProOne, name='ProOne'),
]
