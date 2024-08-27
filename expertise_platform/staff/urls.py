# staff/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('<int:pk>/', views.staff_profile, name='staff_profile'),
]
