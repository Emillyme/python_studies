import random
import time

def menu():
    print('''
    Bem vindo ao JOKENPO!
    Escolha sua defesa!

[0] Pedra
[1] Papel
[2] Tesoura
    ''')
    return int(input('Digite aqui: '))


def main():
    opcoes = {0: 'PEDRA', 1: 'PAPEL', 2: 'TESOURA'}

    while True:
        bot_escolha = random.randint(0, 2)
        escolha_usuario = menu()
        if bot_escolha == 0:
            if escolha_usuario == bot_escolha:
                print(f'empate, você jogou {opcoes[escolha_usuario]} e o bot {opcoes[bot_escolha]}')
            if escolha_usuario == 1:
                print(f'Você ganhou!! Você jogou {opcoes[escolha_usuario]} e o bot {opcoes[bot_escolha]} ')
            if escolha_usuario == 2:
                print(f'Você perdeu, o bot jogou {opcoes[bot_escolha]}')

        if bot_escolha == 1:
            if escolha_usuario == bot_escolha:
                print(f'empate, você jogou {opcoes[escolha_usuario]} e o bot {opcoes[bot_escolha]}')
            if escolha_usuario == 2:
                print(f'Você ganhou!! Você jogou {opcoes[escolha_usuario]} e o bot {opcoes[bot_escolha]} ')
            if escolha_usuario == 0:
                print(f'Você perdeu, o bot jogou {opcoes[bot_escolha]}')

        if bot_escolha == 2:
            if escolha_usuario == bot_escolha:
                print(f'empate, você jogou {opcoes[escolha_usuario]} e o bot {opcoes[bot_escolha]}')
            if escolha_usuario == 0:
                print(f'Você ganhou!! Você jogou {opcoes[escolha_usuario]} e o bot {opcoes[bot_escolha]} ')
            if escolha_usuario == 1:
                print(f'Você perdeu, o bot jogou {opcoes[bot_escolha]}')
        time.sleep(2)


if __name__ == '__main__':
    main()