from django.conf.urls import path

from . import views

urpatterns = [
    path('' ,views.index,name='index'),
]
