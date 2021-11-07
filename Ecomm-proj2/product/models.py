from django.db import models
from vendor.models import Vendor
class Category(models.Model):
    Category_Name=models.CharField(max_length=40)
    Category_Discription=models.CharField(max_length=100)
    def __str__(self):
        return self.Category_Name
# Create your models here.
class Product(models.Model):
    Product_Name=models.CharField(max_length=40)
    Product_Image=models.ImageField(upload_to="images/",null=True,blank=True)   
    Product_Discription=models.CharField(max_length=100)
    Product_Price=models.IntegerField()
    Product_Stock=models.IntegerField()
    Product_Stock_Status=models.BooleanField()
    #vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True)
    Product_Category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Product_Name


