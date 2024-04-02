# 026: Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra "A", em que posição ela aparece
# a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite seu nome: ')).lower()
print(f'No seu nome aparece {nome.count('a')} vezes a letra "a"')
print(f'A primeira letra \'A\' apareceu na posição: {nome.find('a')+1}')
print(f'A primeira letra \'A\' apareceu na posição: {nome.rfind('a')+1}')