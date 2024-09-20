from django.contrib import admin
from .models import Obra, Empresa, Acompanhamento, Material
@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'dt_inicio', 'dt_fim', 'empresa', 'ativo', 'criacao', 'atualizacao')
    search_fields = ('nome', 'descricao')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'endereco', 'telefone', 'ativo', 'criacao', 'atualizacao')
    search_fields = ('nome', 'cnpj')

@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('url', 'desc', 'data', 'ativo', 'criacao', 'atualizacao')
    search_fields = ('url', 'desc')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'dt_recebimento', 'faltando', 'qt_materiais', 'ativo', 'criacao', 'atualizacao')
    search_fields = ('nome', 'descricao')