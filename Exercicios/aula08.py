#imports:
import math
import random
import emoji
import pygame

def exercicios():
    opcao = input('''
    ==================================
        EXERCÍCIOS AULA 7: imports

[1] math
[2] random
[3] emoji
[4] Quebrando um número
[5] Pitagoras
[6] Seno, Cosseno e Tangente
[7] Sorteando os Alunos
[8] Embaralhador de lista 
[9] MP3
    
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
    elif opcao == '6':
        cos_sen_tang()
    elif opcao == '7':
        sorteando_alunos()
    elif opcao == '8':
        embaralhando_lista()

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
    cateto1 = float(input('Digite o valor do primeiro cateto: '))
    cateto2 = float(input('Digite o valor do segundo cateto: '))
    # calc_hipo = (cateto1 **2 + cateto2 **2) ** 1/2
    calc_hipo = math.hypot(cateto1, cateto2)

    print(f'O calculo da hipotenusa é {calc_hipo:.2f}')

def cos_sen_tang():
   ang = float(input('Digite um angulo: '))
   seno = math.sin(math.radians(ang))
   cos = math.cos(math.radians(ang))
   tang = math.tan(math.radians(ang))

   print(f'''
    Angulo: {ang}
    -------
    Seno: {seno:.2f}
    Cosseno: {cos:.2f}
    Tangente: {tang:.2f}
    ''')

def sorteando_alunos():
    aluno1 = 'Maria'
    aluno2 = 'Luiz'
    aluno3 = 'Nicolas'
    aluno4 = 'Gravetto'
    alunos = [aluno1, aluno2, aluno3, aluno4]

    sorteador = random.choice(alunos)
    print(f'O aluno sorteado foi o {sorteador}!')

def embaralhando_lista():
    lista = []
    for i in range(6):
        num = input(f'{i} - ')
        lista.append(num)

    random.shuffle(lista)
    print(lista)

def MP3():
    

def main():
    exercicios()

main()