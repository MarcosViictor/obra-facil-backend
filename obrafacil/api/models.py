from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class GerenteDeObra(Base):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Gerente de Obra'
        verbose_name_plural = 'Gerentes de Obra'

    def __str__(self):
        return self.nome
    
    def set_safeword(self, raw_safeword):
        
        self.safeword = make_password(raw_safeword)

    def check_safeword(self, raw_safeword):
        
        return check_password(raw_safeword, self.safeword)
    

class MestreDeObra(Base):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    gerente_de_obra = models.ForeignKey(GerenteDeObra, on_delete=models.CASCADE, related_name='mestres_de_obra')

    class Meta:
        verbose_name = 'Mestre de Obra'
        verbose_name_plural = 'Mestres de Obra'

    def __str__(self):
        return self.nome
       
    def set_safeword(self, raw_safeword):
        
        self.safeword = make_password(raw_safeword)

    def check_safeword(self, raw_safeword):
        
        return check_password(raw_safeword, self.safeword)

class Obra(Base):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    dt_inicio = models.DateTimeField()
    dt_fim = models.DateTimeField()
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    mestre_de_obra = models.ForeignKey(MestreDeObra, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'

    def __str__(self):
        return self.nome

class Empresa(Base):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome

class Acompanhamento(Base):
    url = models.URLField(max_length=200, unique=True)
    desc = models.TextField()
    data = models.DateTimeField()
    mestre_de_obra = models.ForeignKey(MestreDeObra, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Acompanhamento'
        verbose_name_plural = 'Acompanhamentos'

    def __str__(self):
        return self.url

class Material(Base):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    dt_recebimento = models.DateTimeField()
    faltando = models.IntegerField()
    qt_materiais = models.IntegerField()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'

    def __str__(self):
        return self.nome