import random
from time import sleep

numero_escondido = random.randint(0, 5)

print('Computador está pensando em um número de 0 a 5', end='')
for i in range(3):
    sleep(1)
    print('.', end='')

sleep(0.5)
while True:
    tentativa = int(input('\nTente acertar o número: '))
    if tentativa > 5:
        print('Número inválido.')
        continue
    if tentativa == numero_escondido:
        print(f'parabéns, você acertou! O número escondido era {numero_escondido}')
    else:
        print(f'poxa, você errou! O número escondido era {numero_escondido}')
    break
