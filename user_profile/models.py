from django.db import models

# Create your models here.

class WithdrawalMethod(models.Model):
    name = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name or "Unnamed Method"

class WithdrawalProcess(models.Model):
    method = models.ForeignKey(
        WithdrawalMethod,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Withdrawal of {self.amount} using {self.method}"
