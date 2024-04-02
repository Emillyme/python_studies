# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
nome_separado = nome.split()
print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
print(f'Nome com todas as letras ao todo (sem considerar espaços): {len(''.join(nome_separado))}')
print(f'Quantas letras tem o primeiro nome: {len(nome_separado[0])}')