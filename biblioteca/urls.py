from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LivroViewSet, UsuarioViewSet, EmprestimoViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'emprestimos', EmprestimoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]