from django.contrib import admin


# Register your models here.

from .models import User
from .models import order
from .models import orderdetails
from .models import addtocart
admin.site.register(User)
admin.site.register(order)
admin.site.register(orderdetails)
admin.site.register(addtocart)