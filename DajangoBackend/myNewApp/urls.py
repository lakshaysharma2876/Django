from django.urls import path
from . import views

urlpatterns = [
    path('', views.chai_order, name= 'chai_order'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]
