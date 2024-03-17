from itertools import product
import inquirer


def pedir_nome(n_jogador:int, simbolizin:str):
    return input(f'\033[1;37m[{simbolizin}]\033[m Digite o nome do \033[1mjogador {n_jogador}\033[m: ')


def menuzin(pontos_O, pontos_x, n1, n2):
    print(f' \033[1;36mX\033[m = {n1}         \033[1;38mPontos:\033[m {pontos_x}')
    print(f' \033[1;31mO\033[m = {n2}         \033[1;38mPontos:\033[m {pontos_O}\n')


def mostrar_jogo(jogo):
    print('     \033[1;37mA   B   C\033[m')
    for i in range(3):
        print(f' \033[1;37m{i}\033[m   {jogo[i][0]} \033[1m│\033[m {jogo[i][1]} \033[1m│\033[m {jogo[i][2]}')
        if i < 2:
            print("   \033[1m—————————————\033[m")


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


def aparecer_blocotexto(pontos_x, pontos_O, n1, n2):
    try:
        placarzinho = open("placar3.txt", "a")
        dados = f'''JOGADOR X: {n1} PONTOS: {pontos_x}
JOGADOR O: {n2} PONTOS: {pontos_O}\n\n'''
        placarzinho.write(dados)
        placarzinho.close()
        print('Gravado com sucesso')
    except:
        print('Erro no cadastro.')


def ler_historico():
    try:
        with open("placar3.txt", "r") as placar:
            for historico in placar:
                print(historico)
    except FileNotFoundError:
        print('Arquivo não encontrado.')


def main():
    print(f'\n\033[1;35mSEJA BEM-VINDO ao jogo da VELHA!\033[m')
    n1 = pedir_nome(1, 'x')
    n2 = pedir_nome(2, 'o')
    jogador1 = {
        'simbolo': '\033[1;36mX\033[m',
        'nome_jogador': n1}
    jogador2 = {
        'simbolo': '\033[1;31mO\033[m',
        'nome_jogador': n2}  # '\033[1;31mO' # '\033[1;36mX\033[m'
    pontos_O = 0
    pontos_x = 0

    jogo = ([' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '])

    jogador_atual = jogador2['simbolo']

    while True:
        while True:
            print('\n\033[1;45m      JOGO DA VELHA      \033[m')
            menuzin(pontos_O, pontos_x, n1, n2)
            mostrar_jogo(jogo)

            print(f"\n Vez do jogador {jogador_atual}")
            linha, coluna = perguntas()
            if jogo[linha][coluna] == ' ':
                jogo[linha][coluna] = jogador_atual
            else:
                print('Essa posição já está ocupada.')
                continue
            ganhador = ganhar(jogo, jogador_atual)

            if ganhador:
                if jogador_atual == jogador1['simbolo']:
                    pontos_x += 1
                else:
                    pontos_O += 1
                menuzin(pontos_O, pontos_x, n1, n2)
                aparecer_blocotexto(pontos_x, pontos_O, n1, n2)
                break

            if jogador_atual == jogador1['simbolo']:
                jogador_atual = jogador2['simbolo']
            else:
                jogador_atual = jogador1['simbolo']

        # # QUESTIONS PARA FAZER AO JOGADOR PÓS ELE JOGAR
        questions = [
            inquirer.List('escolha', message="Deseja continuar competindo?",
                          choices=['SOU FODÃO!!', 'Sair', 'Histórico de Partidas'])
        ]

        answers = inquirer.prompt(questions)

        if answers['escolha'] == 'SOU FODÃO!!':
            continue

        elif answers['escolha'] == 'Sair':
            print('Saindo...')
            break

        elif answers['escolha'] == 'Histórico de Partidas':
            ler_historico()
            continue


if __name__ == '__main__':
    main()
