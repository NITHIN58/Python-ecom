
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)

class User(AbstractUser):
    STATUS=(
        ('admin','admin'),
        ('customer','customer'),
        ('driver','driver')

    )
    username=models.CharField(max_length=100,null=True,blank=True)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    role=models.CharField(max_length=30,null=True,choices=STATUS)
    postcode=models.IntegerField(null=True,default=None)
    profilepic=models.ImageField(upload_to='Images/',null=True,blank=True)
    password=models.CharField(max_length=30,null=True)
    password2=models.CharField(max_length=30,null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['address','phone','city','postcode']
    objects=UserManager()

    def get_username(self):
        return self.email




class orderdetails(models.Model):
    product_id=models.ForeignKey('product.Product', on_delete=models.CASCADE,null=True)
    product_qty=models.FloatField(null=True)
    product_price=models.IntegerField(null=True)
    subtotal=models.IntegerField(null=True)
    order=models.ForeignKey('order', on_delete=models.CASCADE,null=True)




class order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Accepted','Accepted'),
        ('Out for Delivery','Out for Delivery'),
        ('Order Cancel','Order Cancel'),
        ('Customer Cancel','Customer Cancel'),
        ('Delivered','Delivered'),
        ('Added to Cart','Added to Cart'),
        ('Assigned to Driver','Assigned to Driver')
    )
    order_date=models.DateField(null=True)
    customer_id=models.ForeignKey('User', on_delete=models.CASCADE,null=True)
    vendor_id=models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE,null=True)
    order_total=models.IntegerField(null=True)
    payment_method=models.CharField(default="",max_length=50,null=True)
    delivery_date=models.DateField(null=True)
    status=models.CharField(default="ordered",max_length=50,null=True,choices=STATUS)
    Is_deliverd=models.BooleanField(default=False)
    def get_date(self):
        return self.delivery_date.date()


class addtocart(models.Model):
    cartuser=models.ForeignKey('User', on_delete = models.CASCADE, null=True)
    cartproduct = models.ForeignKey('product.Product', on_delete = models.CASCADE, null=True)
    cartquantity=models.IntegerField(null=True,default=1)

class shippmenst(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    postcode=models.IntegerField(null=True,default=None)

class dbwishlist(models.Model):
    wuser=models.ForeignKey('User', on_delete = models.CASCADE, null=True)
    wproduct = models.ForeignKey('product.Product', on_delete = models.CASCADE, null=True)
