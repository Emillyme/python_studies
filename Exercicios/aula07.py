def exercicios():
    opcao = input('''
==================================
        EXERCÍCIOS AULA 7:

[1] Prints e formas de usa-lo 
[2] Operadores
[3] Antecessor e Sucessor
[4] Dobro, Triplo e Raiz Quadrada
[5] Média
[6] Conversão: metros para centímetros e milímetros
[7] Tabuada
[8] Conversão Moedas.
[9] Pintando a Parede
[10] Desconto
[11] Salário adicional
[12] Conversao de Temperatura
[13] Aluguel de carros
    
Digite o exercício que você quer ver: ''')

    if opcao == '1':
        printsFormas()
    elif opcao == '2':
        operadores()
    elif opcao == '3':
        anteSuce()
    elif opcao == '4':
        dobroTriploRaiz()
    elif opcao == '5':
        media()
    elif opcao == '6':
        conversao()
    elif opcao == '7':
        tabuada()
    elif opcao == '8':
        conversaoMoedas()
    elif opcao == '9':
        pintandoParede()
    elif opcao == '10':
        desconto()
    elif opcao == '11':
        salarioAdicional()
    elif opcao == '12':
        conversaoTemperatura()
    elif opcao == '13':
        aluguelCarros()


def printsFormas():
    print('='*10) #repete muitas vezes o =
    nome = input('qual é o seu nome? ')

    # print('Prazer em te conhecer {:>20}!'.format(nome))
    # print('Prazer em te conhecer {:20}!'.format(nome))
    # print('Prazer em te conhecer {:^20}!'.format(nome))
    # print('Prazer em te conhecer {:=^20}!'.format(nome))

    #outra maneira:
    print(f'Prazer em te conhecer {nome:>20}!')
    print(f'Prazer em te conhecer {nome:20}!')
    print(f'Prazer em te conhecer {nome:^20}!')
    print(f'Prazer em te conhecer {nome:=^20}!')
    print(f'Prazer em te conhecer {nome:#^30}!')
    print(f'Prazer em te conhecer {nome:-^30}!')

def operadores():
    n1 = int(input('digite o valor 1: '))
    n2 = int(input('digite o valor 2: '))
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2
    di = n1 // n2
    e = n1 ** n2

    print(f'a soma é {s}, a multiplicação é {m}, a divisão {d:.2f},'
          f' a divisão inteira é {di} e a exponenciação é {e}!')

def anteSuce():
    num = int(input('Digite um número: '))
    ante = num - 1
    suce = num + 1

    print(f'O sucessor do número {num} é {suce}', end=' ')
    print(f'e seu antecessor é {ante}!')

def  dobroTriploRaiz():
    num = int(input('Digite um número: '))
    dobro = num*2
    triplo = num*3
    raiz = num**(1/2)

    print(f'SOBRE O NÚMERO {num}:\n'
          f'dobro =  {dobro} \n'
          f'triplo =  {triplo}\n'
          f'raiz quadrada = {raiz}')

def media():
    notas = []
    provas = int(input('Quantas provas você deu esse semestre: '))
    for i in range(1, provas+1):
        provas = int(input(f'Digite a {i}° nota: '))
        notas.append(provas)

    soma = sum(notas)  # soma todos os elementos dentro do array
    quantidadeProvas = len(notas)  # fala a quantidade de elementos no array
    media = soma/quantidadeProvas

    print(notas)
    print(f'a media dessas notas é {media}')

    # media = somaDasNotas/quantidade

def conversao():
    metros = int(input('Digite em metros para a conversão: '))
    pCentimentos = metros * 100
    pMilimetros = metros * 1000

    print(f'Metros: {metros} \n'
          f'{metros}m para centimetros: {pCentimentos} \n'
          f'{metros}m para milímetros: {pMilimetros}')

def tabuada():
    num = int(input('Digite o número para fazer a tabuada: '))
    quantidade = int(input('Até que número deseja que vá a tabuada? '))
    for i in range(quantidade+1):
        m = num*i
        print(f'{num} x {i} = {m}')

def conversaoMoedas():
    escolha = (input('''
    =================================
    Escolha a conversão: 
    
    [1] Real(R$) para Dolar(US$)
    [2] Dolar(US$) para Real(R$)
    
    '''))

    if escolha == '2':
        dolares = float(input('Digite quanto dinheiro em DÓLAR você tem: '))
        taxa = 5
        conversao = dolares * taxa
        print(f'Você tem US${dolares} que convertido para reais é R${conversao:.2f}!')

    elif escolha == '1':
        dindin = float(input('Digite quanto dinheiro em REAIS você tem: '))
        dolar = 4.95
        quant = (dindin/dolar)
        print(f'Você pode comprar US${quant:.2f} com seus R${dindin:}')


def pintandoParede():
    largura = int(input('Digite qual a largura da sua parede(m): '))
    altura = int(input('Digite qual a altura da sua parede(m): '))
    area = largura*altura
    pintura = area/2

    print(f'sua parede tem a área de {area} e a quantidade de tinta necessária para a pintura é {pintura:.1f} litros')

def desconto():
    precoOriginal = int(input('Digite o preço original: '))
    desconto = int(input('Digite o desconto que será aplicado: '))
    precoComDesconto = precoOriginal - (precoOriginal * desconto/100)

    print(f'O preço R${precoOriginal:.2f} com desconto de {desconto}%, vai ficar R${precoComDesconto:.2f}!')

def salarioAdicional():
    salarioInicial = float(input('Digite seu salário inicial: '))
    adicional = float(input('Digite a porcentagem do adicional: '))
    precoComAdicional = salarioInicial + (salarioInicial * adicional/100)

    print(f'O seu novo salário é R$ {precoComAdicional:.2f}')

def conversaoTemperatura():
    c = int(input('Digite a temperatura em Celsius: '))
    f = (c * 1.8 + 32)

    print(f'A conversão da temperatura para Fahrenheit é {f}')

def aluguelCarros():
    dias = int(input('Digite quantos dias de carro você percorreu: '))
    km = float(input('Quantidade de km percorridos: '))
    diasPagos = dias * 60
    kmPagos = km * 0.15

    print(f'O preço a pagar pelos dias e km percorridos é R${kmPagos + diasPagos:.2f}')

def main():
    exercicios()

main()