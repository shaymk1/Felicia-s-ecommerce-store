
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('securelogin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include("store.urls")),
    path('carts/', include("carts.urls")),
    path('accounts/', include('accounts.urls')),
    # ORDERS
    path('orders/', include('orders.urls')),
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
