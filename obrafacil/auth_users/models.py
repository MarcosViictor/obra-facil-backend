from django.contrib.auth.models import User
from django.db import models

# Modelo para Gerente de Obra
class GerenteDeObra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    # Outros campos específicos para Gerente de Obra

    def __str__(self):
        return self.nome

# Modelo para Mestre de Obra
class MestreDeObra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gerente = models.ForeignKey(GerenteDeObra, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=255)
    # Outros campos específicos para Mestre de Obra

    def __str__(self):
        return self.nome
