print('=== Exercício 2: Escreva um algoritmo que determine se um número é par ou ímpar ===')
numero = int(input('Insira um número: '))

if (numero) % 2 == 0:
    print('é par')
else:
    print('é impar')


print('=== Exercício 3: Desenvolva um algoritmo que imprima os números de 1 a 10. ===')

lista = []

# in: para CADA elemento vai ser aplicado pipipopop
for lista in (range(1, 11)):
    print(lista)


print('=== Exercício 4: Crie um algoritmo para calcular a média de três números fornecidos pelo usuário. ===')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
media = round((n1 + n2 + n3)/3)

print ( f'A média dos números {n1}, {n2} e {n3} é {media}!')


print('=== Exercício 6: Escreva um algoritmo que leia 5 números e informe o maior deles. ===')

nums = []

for i in range(5): #range: é pra ir adicionando o numero a cada loop
    num = int(input(f'Informe o {i + 1}º número: '))
    nums.append(num) # Adiciona o número à lista nums

maior_numero = max(nums)  # Encontra o maior número na lista usando a função max()
print(f'O maior número é: {maior_numero}')  # Exibe o maior número


print('=== Exercício 7: Desenvolva um algoritmo que some todos os números de 1 a 100.')

soma = 0

for i in range(1, 101):
    #simplicaficado:
    soma += i
    #como é sem ser simplificado:
    # soma = soma + i
    # obs: da o mesmo resultado, porém usar += simplifica

    print(f'A soma de todos os números de {i} a 100 é: {soma}')


print('=== Exercício 9: Escreva um algoritmo que encontre o primeiro número maior que 100 em uma lista.')

lista = [100, 29, 203, 33, 4, 202, 1000, 223, 0]
def encontrar_numero_maior (lista):
    for numX in lista:
        if numX > 100:
            return numX
    return None # Retorna None se não houver número maior que 100 na lista

resultado = encontrar_numero_maior(lista)
print(resultado)


print('=== Exercício 10: Crie um algoritmo que continue a pedir números ao usuário até que ele digite 0')

while True:
    num_u = int(input('Digite um número: '))

    if num_u == 0:
        break

print('=== Exercício 12: Escreva um algoritmo que verifique se uma string é um palíndromo.')



print('=== Exercício 14: Crie um algoritmo para converter temperaturas de Celsius para Fahrenheit.')

#forma simples:
temp_cel = float(input('Digite a temperatura em graus Celsius: '))
calc = (round(temp_cel * 9/5) + 32)

print(f'A temperatura {temp_cel}ºC em Fahrenheit é {calc}ºF')

#forma em function:
temp_celsius = float(input('Digite a temperatura em celsius: '))
def conversao_temp(temp_celsius):
    calc = round(temp_celsius * 9 / 5 + 32)
    return calc

resultado = conversao_temp(temp_celsius)
print(f'A temperatura {temp_celsius}ºC em Fahrenheit é {resultado}ºF')


print('=== Exercício 15: Crie um algoritmo que imprima os primeiros 10 múltiplos de um número fornecido pelo usuário')

num_mul = int(input('Digite um número:'))

for i in range(1, 10 + 1):
    multiplo = num_mul * i
    print(multiplo)

#em função:
    multiplos = []
def encontrar_multiplos (numerox, quantidade):
    for i in range(1, quantidade + 1):
        multiplo_calc = numerox * i
        multiplos.append(multiplo_calc)
    return multiplos

numnum = int(input('Digite o número: '))
quanti = int(input('Digite a quantidade de múltiplos: '))

resultado_multiplos = encontrar_multiplos(numnum, quanti)
print(resultado_multiplos)
