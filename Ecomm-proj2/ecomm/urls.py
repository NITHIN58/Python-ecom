
from django.contrib import admin
from django.urls import path,include
from ekart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ekart.urls')),
    path('', include('product.urls')),
    path('',include('vendor.urls'))

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

