#imports:
import math
import random
import emoji

def exercicios():
    opcao = input('''
    ==================================
        EXERCÍCIOS AULA 7: imports

[1] math
[2] random
[3] emoji
[4] Quebrando um número
[5] Pitagoras
    
Digite o exercício que você quer ver: ''')

    if opcao == '1':
        modulos()
    elif opcao == '2':
        randomm()
    elif opcao == '3':
        emojii()
    elif opcao == '4':
        quebrandoUmNúmero()
    elif opcao == '5':
        pitagoras()

def modulos():
    num = int(input('Digite um número: '))
    raiz = math.sqrt(num)

    print(f'arredondando pra cima(ceil): raiz de {num} é {math.ceil(raiz)}')
    print(f'arredondando pra baixo(floor): raiz de {num} é {math.floor(raiz)}')

def randomm():
    num1 = random.random() #numero aleatório entre 0 e 1
    num2 = random.randint(1, 10)  # numero aleatório inteiro
    print(num1, num2)

def emojii():
    print(emoji.emojize(':smile:', language='alias'))

def quebrandoUmNúmero():
    num = float(input('Digite um número real: '))
    transInt = math.trunc(num) #corta para o

    print(f'O número real {num} em inteiro ficaria {transInt}')

def pitagoras():
    #(a**2 = b**2 + c**2)
    cateto1 = int(input('Digite o valor do primeiro cateto: '))
    cateto2 = int(input('Digite o valor do segundo cateto: '))
    calcHipo = (math.pow(cateto1,2) + math.pow(cateto2, 2))
    

def main():
    exercicios()

main()