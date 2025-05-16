from django.urls import path
from . import views

urlpatterns = [
    path('performance-test/', views.db_performance_test, name='db_performance_test'),
    path('performance-dashboard/', views.performance_dashboard, name='performance_dashboard'),
]
