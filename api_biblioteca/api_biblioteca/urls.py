from django.contrib import admin
from django.urls import path, include
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),  # sua API REST
    path('', views.index, name='index'),
    path('livros/', views.livros_page, name='livros'),
    path('usuarios/', views.usuarios_page, name='usuarios'),
]