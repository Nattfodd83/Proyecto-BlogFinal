from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', null=True, blank=True)
    
    def __str__(self):
        return f'Imagen de: {self.user}'


class Perfil(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    red_social=models.URLField()
    descripcion=models.TextField()

    def __str__(self):
        return self.user.username