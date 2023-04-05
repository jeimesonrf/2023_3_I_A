class Cachorro:

    def __init__(self, nome, idade, tutor, raca):
        self.nome = nome
        self.idade = idade
        self.tutor = tutor
        self.raca = raca
        self.latir()
    
    def comer(self):
        print(f'{self.nome} está comendo')
    
    def latir(self):
        print(f'{self.nome} está latindo')
    
    def dormir(self):
        print(f'{self.nome} está dormindo')
    
    def acordar(self):
        self.dormir()
        print(f'{self.nome} vai acordar')


if __name__ == "__main__":
    pandora = Cachorro("Pandora", 3, "Luiz", "SRD")
    pandora.dormir()
    pandora.comer()
    pandora.latir()
    pandora.latir()
    pandora.latir()
    leia = Cachorro("Leia", 5, "Jeimeson", "SRD")
    leia.dormir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    leia.latir()
    pandora.acordar()
    leia.acordar()
