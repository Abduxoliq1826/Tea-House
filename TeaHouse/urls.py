from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('manager/', include('main.manager.urls')),
    path('director/', include('main.director.urls')),
    path('cooker/', include('main.cooker.urls')),
    path('waiter/', include('main.waiter.urls')),
    path('api/', include('api.urls')),
    path('call_center/', include('main.call-center.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)