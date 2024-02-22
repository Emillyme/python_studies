#imports:
from time import sleep


# Função para exibir o menu e ter a escolha:
def exibir_menu():
    print(f'''
         Bem - vindo ao     
     MERCADINHO DO CLEBINHO!     

        Menu de Seleção:    
     1. Selecionar produtos    
     2. Pagamento     
     3. Sair
    ''')
    return input(f'Digite uma opção: ')


# Função para escolher os itens do mercadinho e calcular o total:
def selecionar_itens(itens, precos):
    total = 0

    print('Selecione o(s) item(s) de seu interesse: ')
    while True:
        for i, (item, preco) in enumerate(zip(itens, precos), start=1):
            print(f'{i}. {item} - R${preco}')
        print(f'\nValor atual no seu carrinho = R${total:.2f}\n')

        opcao = input('Digite um item da loja (ou "sair" para finalizar): ')
        if opcao.lower() == 'sair':
            break
        if opcao.isdigit():  # is digit é pra verificar se é um número
            indice = int(opcao) - 1

            if indice < len(itens):
                preco_item_escolhido = precos[indice]
                quantidade = int(input(f'Quantidade de {itens[indice]}: '))
                total += preco_item_escolhido * quantidade
            else:
                print('Não existe essa opção, por favor tente novamente.')
                sleep(0.5)
        else:
            print('Opção inválida, por favor tente novamente.')
            sleep(0.5)

        escolha = input('Deseja continuar a compra? (Digite: Sim ou Não)')
        if escolha.lower() == 'não':
            break

    return total


# Função principal para pagamento:
def pagar_itens(total):
    print(f'O total da compra é: R${total:.2f}')
    print('Formas de pagamento: ')
    print('''
    1. Débito
    2. Crédito
    3. Dinheiro
    ''')
    escolha = input('Escolha a opção: ')
    if escolha in ['1', '2']:
        print('Passando o cartão, um momento.')
        sleep(1)
        print('Aprovando a compra...')
        sleep(1)
        print('PAGAMENTO FEITO!')
        sleep(1)
    elif escolha == '3':
        nota = int(input('Digite a nota em dinheiro: '))
        troco = nota - total
        print(f'Aqui está seu troco: R${troco}')
        print('Volte sempre!')
    else:
        print('Opção inválida.')


# Função principal
def main():
    precos = [5.94, 8.97, 9.75, 240.29]
    itens = ['Cerveja', 'Whisky', 'Tequila', 'Camisa do Corinthias ORIGINAL']
    total = 0

    while True:
        escolha = exibir_menu()
        if escolha == '1':
            total = selecionar_itens(itens, precos)
            if total == 0:
                print('Por favor selecione algum item antes de ir para pagamentos.')
                sleep(1.5)
        elif escolha == '2' and total > 0:
            pagar_itens(total)
            break
        elif escolha == '2' and total == 0:
            print('Por favor selecione algum item antes de ir para pagamentos.')
            sleep(1.5)
        elif escolha == '3':
            print('Obrigado pela visita!')
            print('Saindo.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            break


# Inicia o programa:
main()
