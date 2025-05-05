from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('borrar_tarea/<int:id>/', views.borrar_tarea, name='borrar_tarea'),
]
