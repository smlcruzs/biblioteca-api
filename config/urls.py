from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from biblioteca.views import LivroViewSet, UsuarioViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'usuarios', UsuarioViewSet)

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Biblioteca API",
        default_version='v1',
        description="API para gerenciamento de livros e usuários",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
