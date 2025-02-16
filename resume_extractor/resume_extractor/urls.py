from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('extractor.urls')),  # Homepage
    path('api/', include('extractor.urls')),  # API routes
]
