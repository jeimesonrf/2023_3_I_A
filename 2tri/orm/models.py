import peewee

db = peewee.SqliteDatabase('codigo_avulso.db')


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente
        database = db

class Author(BaseModel):

    """
    Classe que representa a tabela Author
    """
    # A tabela possui apenas o campo 'name', que receberá o nome do autor sera unico
    name = peewee.CharField(unique=True)


class Book(BaseModel):
    """
    Classe que representa a tabela Book
    """

    # A tabela possui apenas o campo 'title', que receberá o nome do livro
    title = peewee.CharField(unique=True)

    # Chave estrangeira para a tabela Author
    author = peewee.ForeignKeyField(Author)


if __name__ == '__main__':
    try:
        Author.create_table()
        print("Tabela 'Author' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Author' ja existe!")

    try:
        Book.create_table()
        print("Tabela 'Book' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Book' ja existe!")