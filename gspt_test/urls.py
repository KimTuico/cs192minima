from django.urls import path

from . import views

app_name = 'gspt_test'
urlpatterns = [
    path('', views.index, name = 'index'),
]