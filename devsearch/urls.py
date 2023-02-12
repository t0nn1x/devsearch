from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is for media files (images)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # this is for static files (css, js) 
