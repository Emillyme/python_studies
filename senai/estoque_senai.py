import time


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
    return int(input('\nEscolha o item que deseja acessar: '))


def opcao_menu(itens_nome, indice_item):
    escolha_usuario = int(input(f'''
O que deseja fazer o com o item {itens_nome[int(indice_item)]}?
[0] Adicionar
[1] Excluir
[2] Manter e SAIR
'''))
    return escolha_usuario


def excluir_itens(indice_item, itens_quantidade):
        quantidade = int(input('Quantos deseja excluir?'))
        itens_quantidade[indice_item] -= quantidade
        print('Itens removidos!')

        if quantidade >= itens_quantidade[indice_item]:
            itens_quantidade[indice_item] = 0


def adicionar_itens(indice_item, itens_quantidade):
            quantidade = int(input('Quantos deseja adicionar?'))
            itens_quantidade[indice_item] += quantidade
            print('Adicionado!')


def main():
    itens_nome = ['Computador', 'Teclados', 'Coletores', 'Monitores', 'Balanças', 'Leitores óticos']
    itens_quantidade = [10, 10, 10, 10, 10, 10]

    while True:
        try:
            indice_item = menu(itens_quantidade)
            escolha_do_usuario = opcao_menu(itens_nome, indice_item)

            if escolha_do_usuario == 0:
                adicionar_itens(indice_item, itens_quantidade)
            elif escolha_do_usuario == 1:
                excluir_itens(indice_item, itens_quantidade)
            if escolha_do_usuario == 2:
                print('Saindo...')
                time.sleep(1)
                break
        except ValueError:
            print('Inválido.')
        except IndexError:
            print('Inválido.')


if __name__ == '__main__':
    main()