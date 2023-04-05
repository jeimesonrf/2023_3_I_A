from models import Author, Book

# Inserimos um autor de nome "H. G. Wells" na tabela 'Author'
author_1 = Author.create(name='H. G. Wells')

# Inserimos um autor de nome "Julio Verne" na tabela 'Author'
author_2 = Author.create(name='Julio Verne')

book_1 = {
    'title': 'A Máquina do Tempo',
    'author_id': author_1,
}

book_2 = {
    'title': 'Guerra dos Mundos',
    'author_id': author_1,
}

book_3 = {
    'title': 'Volta ao Mundo em 80 Dias',
    'author_id': author_2,
}

book_4 = {
    'title': 'Vinte Mil Leguas Submarinas',
    'author_id': author_1,
}

books = [book_1, book_2, book_3, book_4]

# Inserimos os quatro livros na tabela 'Book'
Book.insert_many(books).execute()
