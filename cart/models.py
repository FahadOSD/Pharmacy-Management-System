from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Accounts
from drug.models import Drug
from user_role.models import UserRole

class Cart(models.Model):
    buyer_id = models.OneToOneField(Accounts, on_delete=models.CASCADE, unique=True)
    total_cost = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.buyer_id.org_name}"
    
    def save(self, *args, **kwargs):
        if UserRole.objects.filter(acc_id=self.buyer_id, role=UserRole.SELLER).exists():
            raise ValidationError("A company cannot have a cart.")

        super().save(*args, **kwargs)

        # Recalculate the total cost whenever the cart is saved
        self.total_cost = sum(item.item_cost for item in self.cartitem_set.all())
        super().save(update_fields=['total_cost'])

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_cost = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cart {self.cart_id.buyer_id.org_name}: {self.drug_id.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        self.item_cost = self.drug_id.price * self.quantity
        super().save(*args, **kwargs)


        self.cart_id.total_cost = sum(item.item_cost for item in self.cart_id.cartitem_set.all())
        self.cart_id.save(update_fields=['total_cost'])
