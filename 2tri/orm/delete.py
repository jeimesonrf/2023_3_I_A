
from models import Author, Book

# Buscamos o livro que desejamos excluir do banco
book = Book.get(Book.title == "Guerra dos Mundos")

# Excluimos o livro do banco
book.delete_instance()
