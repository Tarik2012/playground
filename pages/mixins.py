from django.shortcuts import redirect
from django.urls import reverse_lazy

class StaffRequiredMixin:
    """Mixin que requiere que el usuario sea staff."""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:  # Verifica si el usuario es staff
            return redirect(reverse_lazy('admin:login'))  # Redirige al login del administrador
        return super().dispatch(request, *args, **kwargs)
