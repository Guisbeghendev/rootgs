# autenticad/admin.py

from django.contrib import admin
from .models import UserExtended  # Atualize aqui para UserExtended

admin.site.register(UserExtended)  # Registre o modelo UserExtended
