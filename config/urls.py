from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from biblioteca.views import index, livros_page, usuarios_page, emprestimos_page

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
    path('api/', include('biblioteca.urls')),  # ← usa o urls.py da biblioteca
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', index, name='index'),
    path('livros/', livros_page, name='livros'),
    path('usuarios/', usuarios_page, name='usuarios'),
    path('emprestimos/', emprestimos_page, name='emprestimos'),
]