from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# borrar imagen de perfil antigua

def custom_upload_to(instance, filename):
    # Verifica si el objeto ya existe en la base de datos
    if instance.pk:
        try:
            # Obtiene la instancia anterior del perfil
            old_instance = Profile.objects.get(pk=instance.pk)
            # Elimina la imagen anterior si existe
            if old_instance.avatar:
                old_instance.avatar.delete(save=False)
        except Profile.DoesNotExist:
            # Si no existe, no se hace nada
            pass
    # Retorna la ruta de carga para el nuevo archivo
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to,null=True, blank=True)
    bio = models.TextField(null=True,blank=True)
    link = models.URLField(max_length=200,null=True,blank=True)
    
    class Meta:
        ordering = ["user__username"]
    
    
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        # Crear el perfil del usuario automáticamente
        Profile.objects.create(user=instance)
    