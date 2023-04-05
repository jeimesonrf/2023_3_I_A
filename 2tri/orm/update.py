from models import Author, Book

new_author = Author.get(Author.name == 'Julio Verne')
book = Book.get(Book.title=="Vinte Mil Leguas Submarinas")

# Alteramos o autor do livro
book.author = new_author

# Salvamos a alteração no banco
book.save()
