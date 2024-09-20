from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GerenteDeObra, MestreDeObra
from django.contrib.auth import authenticate
# Serializer para registro de Gerente de Obra
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class GerenteDeObraRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GerenteDeObra
        fields = ['user', 'nome']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        gerente = GerenteDeObra.objects.create(user=user, **validated_data)
        return gerente
    

# Serializer para registro de Mestre de Obra
class MestreDeObraRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)  # Agora o user é um UserSerializer
    gerente = serializers.PrimaryKeyRelatedField(queryset=GerenteDeObra.objects.all(), required=False)

    class Meta:
        model = MestreDeObra
        fields = ['user', 'gerente', 'nome']

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)  # Pega os dados do user, se houver
        if user_data:
            user = User.objects.create_user(**user_data)  # Cria um novo usuário
        else:
            user = self.context['request'].user  # Usa o usuário autenticado, se nenhum for passado

        mestre = MestreDeObra.objects.create(user=user, **validated_data)
        return mestre
    



from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        attrs['user'] = user
        return attrs
