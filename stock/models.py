from django.db import models
from drug.models import Drug
 
class Stock(models.Model):
    drug_id = models.OneToOneField(Drug, on_delete=models.CASCADE, unique=True)
    quantity = models.IntegerField()
 
    def __str__(self):
        return f"{self.drug_id.name} - {self.quantity}"