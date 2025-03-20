from django.urls import path
from . import views

urlpatterns = [
    path('my-payslips/', views.my_payslips, name='my_payslips'),
    path('payslip/<int:pk>/', views.payslip_detail, name='payslip_detail'),
]
