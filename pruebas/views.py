from django.views.generic import ListView, DetailView
from .models import Pruebas

class PruebasListView(ListView):
    model = Pruebas
    template_name = 'pruebas/pruebas_list.html'  # Cambiado a tu plantilla
    # context_object_name = 'pruebas'  # Nombre del contexto que usarás en la plantilla
    
    
class PruebasDetailView(DetailView):
    model = Pruebas
    template_name = 'pruebas/pruebas_detail.html'  # Plantilla para el detalle
    # context_object_name = 'prueba'  # Nombre del contexto para usar en la plantilla 
    


