from django.urls import path, re_path

from AppTwo import views

urlpatterns = [
    path('', views.help, name='help'),
]
