from rest_framework import serializers
from .models import GerenteDeObra, MestreDeObra, Obra, Empresa, Acompanhamento, Material

class GerenteDeObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = GerenteDeObra
        fields = (
            'id',
            'nome',
            'email',
            'senha',
            'ativo',
            'criacao',
        )
        extra_kwargs = {
            'senha': {'write_only': True},
            'email': {'write_only': True}
        }

class MestreDeObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MestreDeObra
        fields = (
            'id',
            'nome',
            'email',
            'senha',
            'gerente_de_obra',
            'ativo',
            'criacao',
        )
        extra_kwargs = {
            'senha': {'write_only': True},
            'email': {'write_only': True}
        }

class ObraSerializer(serializers.ModelSerializer):
    gerente_de_obra = serializers.CharField(source='mestre_de_obra.gerente_de_obra.nome', read_only=True)
    class Meta:
        model = Obra
        fields = (
            'id',
            'descricao',
            'dt_inicio',
            'dt_fim',
            'empresa',
            'mestre_de_obra',
            'gerente_de_obra'  # Incluído no serializer
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
            'data',
            'mestre_de_obra',
            'gerente_de_obra', 
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