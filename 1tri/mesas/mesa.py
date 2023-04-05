
class Mesa():

    def __init__(self, altura, largura, comprimento):
        self._altura = altura
        self._largura = largura
        self._comprimento = comprimento
        self.area = self.__calc_area()
    
    def __calc_area(self):
        return self._largura * self._comprimento
    
    
if __name__ == '__main__':
    altura = float(input('Entre com a altura da mesa: '))
    largura = float(input('Entre com largura da mesa: '))
    comprimento = float(input('Entre com o comprimento da mesa: '))
    mesa = Mesa(altura, largura, comprimento )
    print(mesa.area)