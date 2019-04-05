from django.urls import path, re_path

from firstappv1 import views
#or u can use "from . import views"

urlpatterns = [
    path('index1/',views.index1, name='index1'),
    path('index2/',views.index2, name='index2'),
    path('<int:indexnumber>/', views.indexnumber, name='indexnumber'),
]
