from django.contrib import admin
from .models import Pruebas  # Importa el modelo Pruebas


class PruebasAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created', 'updated')  # Campos que deseas mostrar en la lista del admin
    search_fields = ('title',)  # Campos por los que puedes buscar
    list_filter = ('created', 'updated')  # Filtros para facilitar la búsqueda
    ordering = ('order', 'title')  # Ordenar por estos campos

# O también puedes registrar el modelo de esta manera:
admin.site.register(Pruebas)
