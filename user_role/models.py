from django.db import models
from accounts.models import Accounts
 
class UserRole(models.Model):
    ADMIN = 'admin'
    SELLER = 'seller'
    BUYER = 'buyer'
 
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (SELLER, 'Company'),
        (BUYER, 'Pharmacy'),
    ]
 
    acc_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['acc_id'], name='unique_role_per_account')
        ]
 
    def __str__(self):
        return f"{self.acc_id.org_name} - {self.role}"