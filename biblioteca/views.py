from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Livro, Usuario, Emprestimo
from .serializers import LivroSerializer, UsuarioSerializer, EmprestimoSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def update(self, request, *args, **kwargs):
        livro = self.get_object()
        usuario_id = request.data.get('usuario_id') or request.query_params.get('usuario_id')
        if str(getattr(livro.cadastrado_por, 'id', None)) != str(usuario_id):
            return Response(
                {'erro': 'Apenas quem cadastrou este livro pode editá-lo.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        livro = self.get_object()
        usuario_id = request.query_params.get('usuario_id')
        if str(getattr(livro.cadastrado_por, 'id', None)) != str(usuario_id):
            return Response(
                {'erro': 'Apenas quem cadastrou este livro pode excluí-lo.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.select_related('livro', 'usuario').all()
    serializer_class = EmprestimoSerializer

    @action(detail=True, methods=['patch'])
    def devolver(self, request, pk=None):
        emprestimo = self.get_object()
        if emprestimo.status == 'devolvido':
            return Response({'erro': 'Este empréstimo já foi devolvido.'}, status=400)
        from django.utils import timezone
        emprestimo.status = 'devolvido'
        emprestimo.data_devolucao = timezone.now().date()
        emprestimo.save()
        return Response(EmprestimoSerializer(emprestimo).data)


# ── FRONTEND ──
def index(request):
    return render(request, 'biblioteca/index.html')

def livros_page(request):
    return render(request, 'biblioteca/livros.html')

def usuarios_page(request):
    return render(request, 'biblioteca/usuarios.html')

def emprestimos_page(request):
    return render(request, 'biblioteca/emprestimos.html')
