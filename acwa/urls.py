from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servey.urls')),  # Corrected 'servey' instead of 'acwa' based on your folder structure
]
