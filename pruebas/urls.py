from django.urls import path
from .views import PruebasListView, PruebasDetailView
from django.conf import settings  # Asegúrate de importar settings
from django.conf.urls.static import static  # Para servir archivos estáticos en desarrollo

# Definir las URLs de la app 'pruebas'
urlpatterns = [
    path('', PruebasListView.as_view(), name='pruebas'),  # Ruta para la lista
    path('<int:pk>/', PruebasDetailView.as_view(), name='prueba_detail'),  # Ruta para el detalle
]

# Añadir configuración para servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
