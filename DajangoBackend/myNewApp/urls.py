from django.urls import path
from . import views

urlpatterns = [
    path('', views.chai_order, name= 'ChaiAppPage'),
]
