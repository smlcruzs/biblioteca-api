import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from biblioteca.models import Livro, Usuario, Emprestimo
from datetime import date, timedelta
import random

# Limpa tudo
Emprestimo.objects.all().delete()
Livro.objects.all().delete()
Usuario.objects.all().delete()

usuarios = [
    Usuario.objects.create(nome="Ana Lima", email="ana.lima@email.com"),
    Usuario.objects.create(nome="Carlos Souza", email="carlos.souza@email.com"),
    Usuario.objects.create(nome="Mariana Costa", email="mariana.costa@email.com"),
    Usuario.objects.create(nome="Pedro Alves", email="pedro.alves@email.com"),
    Usuario.objects.create(nome="Fernanda Reis", email="fernanda.reis@email.com"),
    Usuario.objects.create(nome="Rafael Mendes", email="rafael.mendes@email.com"),
    Usuario.objects.create(nome="Juliana Pinto", email="juliana.pinto@email.com"),
    Usuario.objects.create(nome="Bruno Nunes", email="bruno.nunes@email.com"),
]

livros_data = [
    ("Dom Casmurro", "Machado de Assis", "1899-01-01", "9788535902778"),
    ("Grande Sertão: Veredas", "João Guimarães Rosa", "1956-01-01", "9788535902779"),
    ("O Cortiço", "Aluísio Azevedo", "1890-01-01", "9788535902780"),
    ("Capitães da Areia", "Jorge Amado", "1937-01-01", "9788535902781"),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", "1881-01-01", "9788535902782"),
    ("A Moreninha", "Joaquim Manuel de Macedo", "1844-01-01", "9788535902783"),
    ("Iracema", "José de Alencar", "1865-01-01", "9788535902784"),
    ("O Guarani", "José de Alencar", "1857-01-01", "9788535902785"),
    ("Senhora", "José de Alencar", "1875-01-01", "9788535902786"),
    ("Vidas Secas", "Graciliano Ramos", "1938-01-01", "9788535902787"),
    ("São Bernardo", "Graciliano Ramos", "1934-01-01", "9788535902788"),
    ("Triste Fim de Policarpo Quaresma", "Lima Barreto", "1915-01-01", "9788535902789"),
    ("A Hora da Estrela", "Clarice Lispector", "1977-01-01", "9788535902790"),
    ("Perto do Coração Selvagem", "Clarice Lispector", "1943-01-01", "9788535902791"),
    ("Macunaíma", "Mário de Andrade", "1928-01-01", "9788535902792"),
    ("Angústia", "Graciliano Ramos", "1936-01-01", "9788535902793"),
    ("O Ateneu", "Raul Pompeia", "1888-01-01", "9788535902794"),
    ("Quincas Borba", "Machado de Assis", "1891-01-01", "9788535902795"),
    ("Esaú e Jacó", "Machado de Assis", "1904-01-01", "9788535902796"),
    ("Serafim Ponte Grande", "Oswald de Andrade", "1933-01-01", "9788535902797"),
]

livros = []
for i, (titulo, autor, pub, isbn) in enumerate(livros_data):
    l = Livro.objects.create(
        titulo=titulo,
        autor=autor,
        publicado_em=pub,
        isbn=isbn,
        cadastrado_por=usuarios[i % len(usuarios)]
    )
    livros.append(l)

# Cria alguns empréstimos ativos e devolvidos
for i in range(6):
    Emprestimo.objects.create(
        livro=livros[i],
        usuario=usuarios[i % len(usuarios)],
        status='ativo',
        data_devolucao=date.today() + timedelta(days=random.randint(3, 14))
    )

for i in range(6, 12):
    Emprestimo.objects.create(
        livro=livros[i],
        usuario=usuarios[i % len(usuarios)],
        status='devolvido',
        data_devolucao=date.today() - timedelta(days=random.randint(1, 30))
    )

print(f"✅ {Usuario.objects.count()} usuários")
print(f"✅ {Livro.objects.count()} livros")
print(f"✅ {Emprestimo.objects.count()} empréstimos")
print("Seed concluído!")