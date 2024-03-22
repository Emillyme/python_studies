import time
from itertools import product
import inquirer
import sys



def pedir_nome(n_jogador: int, simbolizin: str):
    return input(f'\033[1;37m[{simbolizin}]\033[m Digite o nome do \033[1mjogador {n_jogador}\033[m: ')


def menuzin(pontos_O, pontos_x, n1, n2):
    print(f' \033[1;36mX\033[m = {n1}         \033[1;38mPontos:\033[m {pontos_x}')
    print(f' \033[1;31mO\033[m = {n2}         \033[1;38mPontos:\033[m {pontos_O}\n')


def mostrar_jogo(jogo):
    print('     \033[1;37mA   B   C   D   E\033[m')
    for i in range(5):
        print(f' \033[1;37m{i}\033[m   {jogo[i][0]} \033[1m│\033[m {jogo[i][1]} \033[1m│\033[m {jogo[i][2]} \033[1m│\033[m {jogo[i][3]} \033[1m│\033[m {jogo[i][4]}')
        if i < 4:
            print("   \033[1m—————————————————————\033[m")


def perguntas():
    while True:
        try:
            coluna = input(f'\nEscolha a coluna (A, B, C, D ou E): ').upper()
            coluna = ord(coluna) - ord('A') # retorna o valor inteiro(numero) de uma string
            linha = int(input(f'Escolha a linha (0, 1, 2, 3 ou 4): '))
            if 0 <= linha <= 4 and 0 <= coluna <= 4:
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
    for i in range(5):
        if all(jogo[i][j] == jogador_atual for j in range(5)) or all(jogo[j][i] == jogador_atual for j in range(5)):
            mostrar_jogo(jogo)
            print(f'Você GANHOU jogador {jogador_atual}')
            return True

    if all(jogo[i][i] == jogador_atual for i in range(5)) or all(jogo[i][4 - i] == jogador_atual for i in range(5)):
        mostrar_jogo(jogo)
        print(f'Você GANHOU jogador {jogador_atual}')
        return True

    for i, j in product(range(5), range(5)):
        if jogo[i][j] == ' ':
            return False

    print('Empate')
    return False


def aparecer_blocotexto(pontos_x, pontos_O, n1, n2):
    try:
        placarzinho = open("placar.txt", "a")
        dados = f'''JOGADOR X: {n1} PONTOS: {pontos_x}
JOGADOR O: {n2} PONTOS: {pontos_O}\n\n'''
        placarzinho.write(dados)
        placarzinho.close()
        print('Gravado com sucesso')
    except:
        print('Erro no cadastro.')


def ler_historico():
    try:
        with open("placar.txt", "r") as placar:
            for historico in placar:
                print(historico)
    except FileNotFoundError:
        print('Arquivo não encontrado.')


def main5():
    print(f'\n\033[1;31mSEJA BEM-VINDO ao VELHA 5 X 5 !\033[m')
    n1 = pedir_nome(1, 'x')
    n2 = pedir_nome(2, 'o')
    jogador1 = {'simbolo': '\033[1;36mX\033[m', 'nome_jogador': n1}
    jogador2 = {'simbolo': '\033[1;31mO\033[m', 'nome_jogador': n2}
    pontos_O = 0
    pontos_x = 0

    while True:
        jogo = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
        jogador_atual = jogador2['simbolo']

        while True:
            print('\n\033[1;41m      JOGO DA VELHA      \033[m')
            menuzin(pontos_O, pontos_x, n1, n2)
            mostrar_jogo(jogo)

            print(f"\n Vez do jogador {jogador_atual}")
            linha, coluna = perguntas()
            if jogo[linha][coluna] == ' ':
                jogo[linha][coluna] = jogador_atual
            else:
                print('Essa posição já está ocupada.')
                time.sleep(0.5)
                continue

            if ganhar(jogo, jogador_atual):
                if jogador_atual == jogador1['simbolo']:
                    pontos_x += 1
                elif jogador_atual == jogador2['simbolo']:
                    pontos_O += 1
                menuzin(pontos_O, pontos_x, n1, n2)
                time.sleep(1.5)
                for i in range(3):
                    print('.', end='')
                    time.sleep(1)
                aparecer_blocotexto(pontos_x, pontos_O, n1, n2)
                break
            else:
                # Alternar entre jogadores
                if jogador_atual == jogador1['simbolo']:
                    jogador_atual = jogador2['simbolo']
                else:
                    jogador_atual = jogador1['simbolo']

            if all(all(cell != ' ' for cell in row) for row in jogo):
                print('Tabuleiro cheio. O jogo terminou em empate.\n')
                time.sleep(1.5)
                break

        questions = [
            inquirer.List('escolha', message="Deseja continuar competindo?",
                          choices=['MAIS UMA PARTIDA QUERIDÃO?', 'Sair e ver Histórico de Partida', 'Voltar para o jogo normal.'])
        ]

        answers = inquirer.prompt(questions)

        if answers['escolha'] == 'Sair e ver Histórico de Partida':
            ler_historico()
            sys.exit()

        elif answers['escolha'] == 'MAIS UMA PARTIDA QUERIDÃO?':
            continue

        elif answers['escolha'] == 'Voltar para o jogo normal.':
            break