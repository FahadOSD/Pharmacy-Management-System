from django.db import models

class Accounts(models.Model):
    org_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    license_no = models.CharField(max_length=50)
    
    def __str__(self):
        return self.org_name
 
