from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^$',views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetail.as_view(), name='detail')
]
