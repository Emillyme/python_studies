def mostrar_jogo(jogo):
    print('     \033[1;37mA   B   C\033[m')
    for i in range(3):
        print(f' \033[1;37m{i}\033[m   {jogo[i][0]} \033[1m│\033[m {jogo[i][1]} \033[1m│\033[m {jogo[i][2]}')
        if i < 2:
            print("   \033[1m—————————————\033[m")


def espaco_vazio(jogo, posicao):
    if(jogo[posicao] == ' '):
        return True
    else:
        return False


def main():
    jogo = ([' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '])

    mostrar_jogo(jogo)
    espaco_vazio(jogo, posicao)


if __name__ == '__main__':
    main()

