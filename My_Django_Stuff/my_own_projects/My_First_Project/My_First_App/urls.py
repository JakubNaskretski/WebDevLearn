from django.urls import path
from My_First_App import views

urlpatterns = [
    path('',views.firstview,name='firstview')
]
