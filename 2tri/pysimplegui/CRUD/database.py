import sqlite3

db_arquivo = './clientes.sqlite3'

class DBCliente():

    def __init__(self):
        self.con = sqlite3.connect(db_arquivo)
        self.cur = self.con.cursor()

    def get_tipo_endereco(self):

        sql = 'SELECT * FROM Tipo_Endereco'

        result = self.cur.execute(sql)
        tipos = result.fetchall()
        for tipo in tipos:
            print(tipo[0],tipo[1])

    def get_tipo_telefone(self):

        sql = 'SELECT * FROM Tipo_Telefone'

        result = self.cur.execute(sql)
        tipos = result.fetchall()
        for tipo in tipos:
            print(tipo[0],tipo[1])


if __name__ == '__main__':
    clientes = DBCliente()
    clientes.get_tipo_endereco()
    clientes.get_tipo_telefone()
    clientes.close()