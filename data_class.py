from dataclasses import dataclass, field, FrozenInstanceError
from typing import Literal

@dataclass(frozen=True)
class Author:
    name:str
    gender:Literal['Masculino','Feminino','Prefiro não dizer']
    about:str
    birth_date:str
    books:list = field(default_factory=list)
    calculate_price_all_books = lambda self : sum(book.price for book in self.books)

@dataclass(frozen=True)
class Books:
    name:str
    publish_date:str
    about:str
    author:Author
    price:float

if __name__=='__main__':
    # Criação de instâncias de Author
    author1 = Author(
        name="João Silva",
        gender="Masculino",
        about="Autor brasileiro de ficção científica.",
        birth_date="1980-05-15"
    )
    print(author1)

    author2 = Author(
        name="Maria Oliveira",
        gender="Feminino",
        about="Escritora renomada de romances históricos.",
        birth_date="1975-09-22"
    )

    print(author2)
    # Criação de instâncias de Books
    book1 = Books(
        name="Viagem ao Desconhecido",
        publish_date="2010-03-10",
        about="Uma jornada épica por mundos desconhecidos.",
        author=author1,
        price=39.98
    )
    print(book1)

    book2 = Books(
        name="Amores Proibidos",
        publish_date="2012-07-18",
        about="Uma história de amor em tempos de guerra.",
        author=author2,
        price=45.79
    )
    print(book2)

    book3 = Books(
        name="O Futuro da Humanidade",
        publish_date="2015-11-05",
        about="Reflexões sobre o destino da raça humana.",
        author=author1,
        price=184.65
    )
    print(book3)

    # Associando livros aos autores
    author1.books.extend([book1, book3])
    author2.books.append(book2)

    # Listas de instâncias
    lista_autores = [author1, author2]
    lista_livros = [book1, book2, book3]

    # Exibindo as listas
    print("Lista de Autores:")
    for autor in lista_autores:
        print(f"Nome: {autor.name}, Gênero: {autor.gender}, Sobre: {autor.about}, Data de Nascimento: {autor.birth_date}, Soma do preço dos livros: ${autor.calculate_price_all_books()}")
        for livro in autor.books:
            print(f"  Livro: {livro.name}, Data de Publicação: {livro.publish_date}, Sobre: {livro.about}, Preço: ${livro.price}")

    print("\nLista de Livros:")
    for livro in lista_livros:
        print(f"Nome: {livro.name}, Data de Publicação: {livro.publish_date}, Sobre: {livro.about}, Autor: {livro.author.name}")

    # Testando alterar o valor de um atributo, deve dar erro!
    try:
        author1.books=[]
    except FrozenInstanceError as e:
        print(f"Ocorreu uma erro na tentativa de alterar o valor de author.books: {str(e)}")