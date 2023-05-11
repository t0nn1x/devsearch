from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('redactor/', views.redactor_dashboard, name='redactor_dashboard'),
]
