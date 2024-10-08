# autenticad/models.py

from django.db import models
from django.contrib.auth.models import User

class UserExtended(User):  # Herança do modelo User
    age = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)  # Ajuste o tamanho conforme necessário
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Salva imagens na pasta 'media/avatars/'
    biography = models.TextField(null=True, blank=True)
    me_conhece_como = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
