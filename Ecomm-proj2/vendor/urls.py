from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from vendor import views

urlpatterns = [
   path("vendor",views.addVender,name="vendor"),
   path("vendorview",views.listVendor,name="vendorview")
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)