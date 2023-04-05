from models import Author, Book

book = Book.get(Book.title == "Volta ao Mundo em 80 Dias").get()
print(book.title)

# Resultado
# * Volta ao Munto em 80 Dias
books = Book.select().join(Author).where(Author.name == 'H. G. Wells')

# Exibe a quantidade de registros que corresponde a nossa pesquisa
print(books.count())

for book in books:
    print(book.title)

# Resultado:
# * A Máquina do Tempo
# * Guerra dos Mundos
# * Vinte Mil Leguas Submarinas
