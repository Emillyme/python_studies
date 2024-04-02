# 023: Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

import time

while True:
    numero = int(input('Digite um número de 0 a 9999: '))
    n = str(numero)
    u = numero // 1 % 10
    d = numero // 10 % 10
    c = numero // 100 % 10
    m = numero // 1000 % 10

    if len(n) > 4:
        print('Número inválido. ')
        time.sleep(1)

    else:
        print(f'unidade: {u}')
        print(f'dezena: {d}')
        print(f'centena: {c}')
        print(f'milhar: {m}')
        break

