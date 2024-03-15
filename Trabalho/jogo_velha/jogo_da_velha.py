# importações
from itertools import product

# def placar(jogador_atual, ganhador):
#

def mostrar_jogo(jogo):
    print('     A   B   C')
    for i in range(3):
        print(f' {i}   {jogo[i][0]} | {jogo[i][1]} | {jogo[i][2]}')
        if i < 2:
            print("   -------------")


def perguntas():
    while True:
        try:
            coluna = input(f'\nEscolha a coluna (A, B ou C): ').upper()
            coluna = ord(coluna) - ord('A')
            linha = int(input(f'Escolha a linha (0, 1 ou 2): '))
            if 0 <= linha <= 2 and 0 <= coluna <= 2:
                return linha, coluna
            else:
                raise IndexError

        except ValueError:
            print('Valor errado. Tente de novo.')
        except IndexError:
            print('Valor errado. Tente de novo.')
        except TypeError:
            print('Valor errado. Tente de novo.')


def ganhar(jogo, jogador_atual):
    for i in range(3):
        if jogo[i][0] == jogo[i][1] == jogo[i][2] == jogador_atual or \
                jogo[0][i] == jogo[1][i] == jogo[2][i] == jogador_atual:
            mostrar_jogo(jogo)
            print(f'Você GANHOU jogador {jogador_atual}')
            return True

    if jogo[0][0] == jogo[1][1] == jogo[2][2] == jogador_atual or \
        jogo[0][2] == jogo[1][1] == jogo[2][0] == jogador_atual:
        mostrar_jogo(jogo)
        print(f'Você GANHOU jogador {jogador_atual}')
        return True

    for i, j in product(range(3), range(3)):
        if jogo[i][j] == ' ':
            return False

    mostrar_jogo(jogo)
    print('Empate')
    return True


def main():
    jogador1 = 'X'
    jogador2 = 'O'
    jogador1_pontos = []
    jogador2_pontos = []

    jogo = ([' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '])
    jogador_atual = jogador2

    while True:
        mostrar_jogo(jogo)
        print(f"\nÉ a vez do jogador {jogador_atual}")
        linha, coluna = perguntas()
        if jogo[linha][coluna] == ' ':
            jogo[linha][coluna] = jogador_atual
        else:
            print('Essa posição já está ocupada.')
            continue
        ganhador = ganhar(jogo, jogador_atual)
        # if ganhador == True:
        #     jogador1_pontos += 1

        if ganhador:
            break

        if jogador_atual == jogador1:
            jogador_atual = jogador2
        else:
            jogador_atual = jogador1


if __name__ == '__main__':
    main()