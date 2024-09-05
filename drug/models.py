from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Accounts
from user_role.models import UserRole  

class Drug(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    acc_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user_role = UserRole.objects.filter(acc_id=self.acc_id, role=UserRole.SELLER).first()
        if not user_role:
            raise ValidationError(f"Account '{self.acc_id}' is not assigned the role 'Company'.")
        super().save(*args, **kwargs)
