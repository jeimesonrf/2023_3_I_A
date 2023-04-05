def ex_00():
    numero = int(input("Digite um número: "))

    if numero >0:
        print('Número positivo')
    elif numero <0:
        print('Número negativo')
    else:
        print('Você digitou o zero')

def ex_01():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')

def ex_02():
    maior = int(input('Digite um número inteiro: '))
    numero_1 = int(input('Digite outro número inteiro: '))
    numero_2 = int(input('Digite mais outro número inteiro: '))
    if numero_1 > maior:
        maior = numero_1
    if numero_2 > maior:
        maior = numero_2
    print(f'{maior} é o maior número')

def ex_03():
    menor = int(input('Digite um número inteiro: '))
    numero_1 = int(input('Digite outro número inteiro: '))
    numero_2 = int(input('Digite mais outro número inteiro: '))
    if numero_1 < menor:
        menor = numero_1
    if numero_2 < menor:
        menor = numero_2
    print(f'{menor} é o maior número')

def ex_04():
    idade = int(input('Qual a sua idade? '))
    if idade >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')

def ex_05():
    peso_ideal = float(input('Qual o seu peso ideal? '))
    peso_atual = float(input('Qual o seu peso atual? '))
    if peso_atual > peso_ideal:
        print('VocÊ está acima do seu peso ideal.')
    else:
        print('Você está no seu peso ideal')

def ex_06():
    nome = input('Qual seu nome? ')
    idade = int(input('Qual sua idade? '))
    if idade >= 16:
        print(f'{nome.upper()} você já pode votar')
    else:
        print(f'{nome.upper()} você ainda não pode votar')

def ex_07():
    numero_1 = float(input('Digite o primeiro número: '))
    numero_2 = float(input('Digite o segundo número: '))
    numero_3 = float(input('Digite o terceiro número: '))
    maior = 0
    if numero_1 > maior:
        maior = numero_1
        l1 = numero_2
        l2 = numero_3
    if numero_2 > maior:
        maior = numero_2
        l1 = numero_1
        l2 = numero_3
    if numero_3 > maior:
        maior = numero_3
        l1 = numero_2
        l2 = numero_1
    
    if maior < l1+l2:
        print('É triângulo')
    else:
        print('Não é triângulo')

def ex_08():
    num1 = int(input("Entre com um número: "))
    num2 = int(input("Entre com outro número: "))
    

