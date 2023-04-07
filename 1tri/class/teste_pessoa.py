import pessoa

def cadastrar():
    name = input('Entre com seu nome: ')
    dayBirth = int(input('Entre com o dia do seu nascimento: '))
    monthBirth = int(input('Entre com o mês do seu nascimento: '))
    YearBirth = int(input('Entre com o ano do seu nascimento: '))

    street = input('Entre com o nome da rua: ')
    number = input('Entre com o número da residência: ')

    p = pessoa.Pessoa(name, dayBirth=dayBirth, monthBirth=monthBirth, yearBirth=YearBirth)

    p.cadastrar_endereco(street, number)
    return p

def cadastrar2():
    name = 'Jeimeson'
    data = {
        'dia':1,
        'mes':11,
        'ano':1977
    }
    endereco = {
        'rua': 'República Argentina',
        'numero': '2376'
    }
    p = pessoa.Pessoa(name,data['dia'], data['mes'],data['ano'])
    return p

if __name__ == '__main__':
    p = cadastrar2()
    print(p.nome, p.idade)
    print(p.endereco)
