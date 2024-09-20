from rest_framework import serializers
from .models import  Obra, Empresa, Acompanhamento, Material

class ObraSerializer(serializers.ModelSerializer):
       class Meta:
        model = Obra
        fields = (
            'id',
            'descricao',
            'dt_inicio',
            'dt_fim',
            'empresa'
        )


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = (
            'id',
            'nome',
            'cnpj',
            'endereco',
            'telefone'
        )

class AcompanhamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompanhamento
        fields = (
            'id',
            'url',
            'desc',
            'data'
        )

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'nome',
            'descricao',
            'dt_recebimento',
            'faltando',
            'qt_materiais'
        )