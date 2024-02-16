
palavra = 'python'
letrasUsuario = []
chances = 7
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letrasUsuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    tentativa = input('\nDigite uma letra: ')
    letrasUsuario.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letrasUsuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'\nParabéns, você ganhou! A palavra era: {palavra}')
else:
    print(f'\nVocê perdeu! A palavra era: {palavra}')
