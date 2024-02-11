
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
