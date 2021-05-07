from django.urls import path
from django.conf.urls import include
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
]