from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class WithdrawalMethod(models.Model):

    name = models.CharField(
        max_length=80, 
        blank=True, 
        null=True,
    )

    def __str__(self):
        return self.name or "Unnamed Method"

class WithdrawalProcess(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]
    
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

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending',
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        default=timezone.now
    ) 

    def __str__(self):
        return f"Withdrawal of {self.amount} using {self.method} - Status: {self.status}"
