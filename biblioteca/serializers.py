from rest_framework import serializers
from .models import Livro, Usuario

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'publicado_em', 'isbn']
        extra_kwargs = {
            'id': {'read_only': True},
            'titulo': {'required': True},
            'autor': {'required': True},
            'isbn': {'required': True}
        }

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'data_cadastro']
        extra_kwargs = {
            'id': {'read_only': True},
            'nome': {'required': True},
            'email': {'required': True}
        }
