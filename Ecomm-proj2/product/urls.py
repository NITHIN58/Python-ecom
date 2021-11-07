from django.urls import path
from product import views,apiViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('/admin',views.dashboard,name='dashboard'),
   path('addadmin',views.addAdmin ,name='addadmin'),
   path('view',views.viewProducts,name="view"),
   path("logout",views.signout,name="signout"),
   path('update<int:userid>',views.updateProduct,name="update"),
   path('delete<int:userid>',views.deletePro,name="deletepro"),
   path('category',views.addCat,name="category"),
   path('filtername',views.filterName,name="byname"),
   path('generate',views.generate ,name="generate"),
   path('filterprice',views.filterprice,name='filterprice'),
   path('filtervendor',views.filterVendor ,name="filtervendor"),
   path('allproducts',apiViews.allProducts),
   path('productreport',views.report ,name="productreport"),
   #classview
   path('product',apiViews.productsclassview.as_view,name="product")
  
 
   

 
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)