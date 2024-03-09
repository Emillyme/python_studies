# Importações de biblioteca:
import random
import time
import threading
import os
import signal

def inicio():
    print('-' * 10, '\033[1;35mBEM-VINDO ao SORTEADOR!\033[m', '-' * 10)
    print('''Há um número escondido nessas redondezas...
            Adivinhe o número!''')


def menu(chances, vida_usuario):
    print(f'\nVocê tem \033[1;31m{chances} chances\033[m...', end=' ')
    print(f'Sua vida:\033[1;33m {vida_usuario}\033[m')

    return int(input('Digite sua tentativa: '))


def sortear_numero():
    numero_sorteado = random.randint(1, 100)
    return numero_sorteado


def perder_vida(numero_escondido, chute):
    if chute > numero_escondido:
        vida_perdida = chute - numero_escondido
    else:
        vida_perdida = numero_escondido - chute

    return vida_perdida


def controlar_tempo():
    gid = os.getpid()
    time.sleep(10)
    print('Seu tempo acabou!')
    os.kill(gid, signal.SIGTERM)

def main():
    gid = os.getpid()
    chances = 4
    vida_perdida = 0
    vida_usuario = 100

    inicio()
    numero_escondido = sortear_numero()
    tempo = threading.Thread(target=controlar_tempo)
    tempo.start()

    while True:
        chances -= 1
        vida_usuario = vida_usuario - vida_perdida

        if chances == 0 or vida_usuario <= 0:
            if vida_usuario <= 0:
                print(f'\n Você perdeu! Sua vida acabou. O número secreto era:  {numero_escondido}')
            elif chances == 0:
                print(f'\nVocê perdeu! Suas chances acabaram! \n O número era {numero_escondido}.')
            break

        chute = menu(chances, vida_usuario)

        if chute == numero_escondido:
            print(f'\nParabéns! Você acertou! O número era {numero_escondido}.')
            break
        else:
            vida_perdida = perder_vida(numero_escondido, chute)
    os.kill(gid, signal.SIGTERM)

if __name__ == '__main__':
    main()
