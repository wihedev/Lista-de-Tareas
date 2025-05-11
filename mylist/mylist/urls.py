from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarea/', include('tarea.urls')),
    path('', include('tarea.urls')),
]
