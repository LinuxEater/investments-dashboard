from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('expenses/', views.expenses_view, name='expenses'),
]