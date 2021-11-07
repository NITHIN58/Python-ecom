from django.db import models

# Create your models here.
class  Vendor(models.Model):
    branch=models.CharField(max_length=20)
    vendor_name=models.CharField(max_length=20)
    phone_number=models.IntegerField(null=True)
    email=models.EmailField(max_length=40)
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.username