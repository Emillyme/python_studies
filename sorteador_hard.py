# Importações de biblioteca:
import random
import threading
import time


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


def main():
    tempo_inicial = time.time()
    chances = 4
    # ganhou = False
    vida_perdida = 0
    vida_usuario = 100

    threading.Thread(inicio())


    numero_escondido = sortear_numero()

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
            # menu(chances, vida_usuario)
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial

        if tempo_decorrido >= 10:
            print(f'Você perdeu muito tempo. O número era {numero_escondido}')
            break

if __name__ == '__main__':
    main()