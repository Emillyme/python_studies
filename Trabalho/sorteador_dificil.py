#Importações de biblioteca:
import random
import time
import threading
import signal
import os


def inicio():
    print(' ' * 12, '\033[39mMODO\033[m \033[1;35mFÁCIL\033[m \033[39mATIVADO!\033[m')
    print('-' * 10, '\033[1;35mBEM-VINDO ao SORTEADOR!\033[m', '-' * 10)
    print('''Há um \033[4;37mnúmero escondido\033[m nessas redondezas...
            Adivinhe o número!''')


def menu(chances, vida_usuario, cores_chances):
    print(f'\nVocê tem {cores_chances}{chances} chances\033[m...', end=' ')
    print(f'Sua vida:\033[1;33m {vida_usuario}\033[m')

    return int(input('\033[1;39mDigite sua tentativa: \033[m'))


def sortear_numero():
    numero_sorteado = random.randint(1, 100)
    return numero_sorteado


def perder_vida(numero_escondido, chute):
    vida_perdida = abs(numero_escondido - chute)
    return vida_perdida


def controlar_tempo():
    gid = os.getpid()
    time.sleep(10)
    print('Seu tempo acabou!')
    os.kill(gid, signal.SIGTERM)


def main():
    gid = os.getpid()
    cor_chances = ['\033[1;31m', '\033[1;31m', '\033[1;33m', '\033[1;32m']
    chances = 4
    vida_perdida = 0
    vida_usuario = 100

    inicio()
    numero_escondido = sortear_numero()
    tempo = threading.Thread(target=controlar_tempo)
    tempo.start()

    while True:
        try:
            cores_chances = cor_chances[chances - 1]
            chances -= 1
            vida_usuario = vida_usuario - vida_perdida
            if chances == 0 or vida_usuario <= 0:
                if vida_usuario <= 0:
                    print('-' * 45)
                    print(f'\nVocê perdeu! Sua vida acabou. \n\033[1;34mO número era {numero_escondido}\033[m')
                elif chances == 0:
                    print('-' * 45)
                    print(f'\nVocê perdeu! Suas chances acabaram! \n\033[1;34mO número era {numero_escondido}\033[m.')
                break

            chute = menu(chances, vida_usuario, cores_chances)

            if chute == numero_escondido:
                print('-' * 45)
                print(f'\nParabéns! Você acertou! \n\033[1;34mO número era {numero_escondido}\033[m.')
                break
            else:
                vida_perdida = perder_vida(numero_escondido, chute)
        except ValueError:
            print('\033[1;31mVocê digitou algo não esperado.\033[m')
            time.sleep(1)
        continue
    os.kill(gid, signal.SIGTERM)


if __name__ == '__main__':
    main()