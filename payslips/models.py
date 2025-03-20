from django.db import models
from django.contrib.auth.models import User

class Payslip(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.username} - {self.pay_date}"
