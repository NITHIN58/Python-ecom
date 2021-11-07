"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from ekart import views,apiViews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('reg',views.registration,name='reg'),
    path("",views.temp ,name='home'),
    path("login",views.user_login,name='login'),
    path('logout',views.signout,name="signout"),
    path("updatepass",views.updatepass ,name="updatepass"),
    path("myaccount",views.myaccount ,name="myaccount"),
    path('customer',views.Addcustomer,name="customer"),
    path('viewcustomer',views.viewcustomer,name="viewcustomer"),
    path('viewOrder',views.viewOrder ,name='viewOrder'),
    path('dashtotal',views.dashboardfront,name='dashtotal' ),
    path('orderstatus',views.getorder,name='orderstatus'),
    path('filterbyid',views.filterbyid,name='filterbyid'),
    path('filterorderdate',views.filtorderbydate,name='filterorderdate'),
    path('showalluser',apiViews.showallusers),
    path('showbyemail',apiViews.showuserByemail),
    path('showallorder',apiViews.showAllOrders),
    path('postcustomer',apiViews.addcustomer),
    path('delete<str:user>',apiViews.deleteuser),
    path('update<str:user>',apiViews.updateuser),
    path('signup',apiViews.signupView ,name='signup'),
    path("wishlist",views.wishlist,name='wishlist'),
    path("addwishlist<int:userid>",views.addwishlist,name='addwishlist'),
    path("deletewishlist<int:userid>",views.deletewishlist,name='deletewishlist'),
     path('viewmyaccount',views.myaccount ,name='viewmyaccount'),
    #frontent list
    path('listproduct',views.listProducts,name='listproduct'),
    #path('cart',views.cart ,name="cart")
    path('cartadd<int:userid>',views.cartadd ,name="cartadd"),
    path('viewcart',views.viewcart,name="viewcart"),
    path("deletecart<int:userid>",views.deletecart,name='deletecart'),
    path('checkout',views.checkout ,name="checkout"),
    #path('placeorder',views.placeorder,name="placeorder")
    path("buynow<int:prid>",views.buynow,name='buynow'),


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
