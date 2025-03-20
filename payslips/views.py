from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payslip

@login_required
def my_payslips(request):
    payslips = Payslip.objects.filter(employee=request.user)
    return render(request, 'payslips/my_payslips.html', {'payslips': payslips})

@login_required
def payslip_detail(request, pk):
    payslip = get_object_or_404(Payslip, pk=pk, employee=request.user)
    return render(request, 'payslips/payslip_detail.html', {'payslip': payslip})
