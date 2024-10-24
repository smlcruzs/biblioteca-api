from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
