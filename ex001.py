import time

while True:
    nome1 = input('Coloque o nome do aluno um: ')
    nota_aluno1 = int(input(f'digite a nota do aluno {nome1}:'))
    print(f'Aluno: {nome1}\n Nota: {nota_aluno1}')
    time.sleep(1)

    nome2 = input('Coloque o nome do aluno dois: ')
    nota_aluno2 = int(input(f'digite a nota do aluno {nome2}: '))
    print(f'Aluno: {nome2}\n Nota: {nota_aluno2}')
    time.sleep(1)

    pergunta = str(input('deseja calcular a média? sim[s] não[n]'))
    if pergunta == ' ' or not pergunta in {'s', 'n'}:
             print('Por favor responde s ou n ')
             continue
    elif pergunta == 's':
            cal = round(nota_aluno1 + nota_aluno2)/2
            print(f'a média entre as duas notas seria {cal}')
            break
    else:
            print('finalizando...')
            break