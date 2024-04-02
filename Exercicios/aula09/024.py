# 024: Crie um programa que leia o nome de uma cidade diga
# se ela começa ou não com o nome "SANTO".

cidade = input('Digite uma cidade: ').strip()
cidade = cidade.lower()
cidade_separada = cidade.split()

if cidade_separada[0] == 'santo':
    print('Começa com Santo')
else:
    print('Não começa com Santo')