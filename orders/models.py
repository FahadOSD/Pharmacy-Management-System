from django.db import models
from accounts.models import Accounts
from cart.models import Cart


class Order(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
 
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    seller_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
 
    def __str__(self):
        return f"Request {self.id} for {self.seller_id.name} - {self.status}"
    
    def save(self, *args, **kwargs):
        self.total_cost = self.cart_id.total_cost
        super().save(*args, **kwargs)