from datetime import datetime


class Pessoa():

    def __init__(self, name, dayBirth, monthBirth, yearBirth):
        self.nome = name
        self.data_nascimento = datetime(yearBirth, monthBirth, dayBirth)
        self.idade = self.calcular_idade()
        self.endereco = ''

    def calcular_idade(self):
        today = datetime.now()
        return int((today-self.data_nascimento).days//365.2425)

    def cadastrar_endereco(self, rua, numero):
        self.endereco = f'{rua}, {numero}'
