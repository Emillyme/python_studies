def menu(itens_quantidade):
    print('\033[1;34m ' * 6, 'SISTEMA DE INVENTÁRIO\033[m','''
    \033[1;33mItens              Quantidade\033[m
    [0] COMPUTADOR              \033[1;38m{}\033[m
    [1] TECLADOS                \033[1;38m{}\033[m
    [2] COLETORES               \033[1;38m{}\033[m
    [3] MONITORES               \033[1;38m{}\033[m
    [4] BALANÇAS                \033[1;38m{}\033[m
    [5] LEITORES ÓTICOS         \033[1;38m{}\033[m
    '''.format(*itens_quantidade))


def opcao_menu(itens_nome):
    item_escolha = input('Escolha o item que deseja acessar: ')
    escolha_usuario = int(input(f'''
O que deseja fazer o com o item {itens_nome[int(item_escolha)]}?
[0] Adicionar
[1] Excluir
[3] Manter
'''))
    return escolha_usuario, item_escolha


def main():
    itens_nome = ['Computador', 'Teclados', 'Mouse', 'Coletores', 'Monitores', 'Balanças', 'Leitores óticos']
    itens_quantidade = [10, 10, 10, 10, 10, 10]

    while True:
        menu(itens_quantidade)
        escolha_usuario = opcao_menu(itens_nome)


if __name__ == '__main__':
    main()