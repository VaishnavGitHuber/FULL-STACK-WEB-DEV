# institutions/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.institution_list, name='institution_list'),
    path('<int:pk>/', views.institution_profile, name='institution_profile'),
    path('<int:pk>/post-requirement/', views.post_requirement, name='post_requirement'),
]
