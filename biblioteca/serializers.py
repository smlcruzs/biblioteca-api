from rest_framework import serializers
from .models import Livro, Usuario, Emprestimo


class LivroSerializer(serializers.ModelSerializer):
    cadastrado_por_nome = serializers.CharField(
        source='cadastrado_por.nome', read_only=True
    )

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'publicado_em', 'isbn', 'cadastrado_por', 'cadastrado_por_nome']
        extra_kwargs = {
            'id': {'read_only': True},
            'titulo': {'required': True},
            'autor': {'required': True},
            'isbn': {'required': True},
            'cadastrado_por': {'required': True},
        }


class UsuarioSerializer(serializers.ModelSerializer):
    total_emprestimos = serializers.IntegerField(
        source='emprestimos.count', read_only=True
    )
    total_livros = serializers.IntegerField(
        source='livros_cadastrados.count', read_only=True
    )

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'data_cadastro', 'total_emprestimos', 'total_livros']
        extra_kwargs = {
            'id': {'read_only': True},
            'nome': {'required': True},
            'email': {'required': True},
        }


class EmprestimoSerializer(serializers.ModelSerializer):
    livro_titulo = serializers.CharField(source='livro.titulo', read_only=True)
    livro_autor = serializers.CharField(source='livro.autor', read_only=True)
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)

    class Meta:
        model = Emprestimo
        fields = [
            'id', 'livro', 'livro_titulo', 'livro_autor',
            'usuario', 'usuario_nome',
            'data_emprestimo', 'data_devolucao', 'status'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'data_emprestimo': {'read_only': True},
            'status': {'read_only': True},
        }

    def validate_livro(self, livro):
        if Emprestimo.objects.filter(livro=livro, status='ativo').exists():
            raise serializers.ValidationError("Este livro já está emprestado.")
        return livro