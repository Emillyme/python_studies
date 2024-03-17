import time

def menu(veiculos, vagas, valor_estacionamento):
    print(' ' * 5 + '\033[1;34mESTACIONAMENTO\033[m')
    print(' ' * 5 + '\033[1;33mR$12.00 POR VAGA\033[m')
    print('\033[1;32mVEICULOS         VAGAS\033[m')
    for i in range(len(vagas)):
        print(f'\033[1;31m{i}.\033[m {veiculos[i]:<15} {vagas[i]}')
    print(' ' * 10 + f'VALOR: R${valor_estacionamento:.2f}')


def escolher_carro(vagas):
    quantidade_carro = int(input('Quantas vagas de carro você quer? '))
    if quantidade_carro > vagas[0]:
        print("Desculpe, não há vagas suficientes para carros.")
        return 0
    else:
        vagas[0] -= quantidade_carro
        return quantidade_carro


def escolher_moto(vagas):
    quantidade_moto = int(input('Quantas vagas de moto você quer? '))
    if quantidade_moto > vagas[1]:
        print("Desculpe, não há vagas suficientes para motos.")
        return 0
    else:
        vagas[1] -= quantidade_moto
        return quantidade_moto


def valor(valor_estacionamento, quantidade):
    contar = 12 * quantidade
    return valor_estacionamento + contar


def retirar_carro(vagas, quantidade):
    vagas[0] += quantidade


def retirar_moto(vagas, quantidade):
    vagas[1] += quantidade


def main():
    veiculos = ['CARRO', 'MOTO']
    vagas = [30, 15]
    valor_estacionamento = 0

    while True:
        menu(veiculos, vagas, valor_estacionamento)
        escolha = int(input('Escolha seu veículo (0 - Carro, 1 - Moto): '))
        if escolha == 0:
            quantidade = escolher_carro(vagas)
        elif escolha == 1:
            quantidade = escolher_moto(vagas)
        valor_estacionamento = valor(valor_estacionamento, quantidade)

        time.sleep(2)
        escolha2 = input('Deseja retirar o veiculo? (s/n)')
        if escolha2.lower() == 's':
            if escolha == 0:
                retirar_carro(vagas, quantidade)
            else:
                retirar_moto(vagas, quantidade)
            valor_estacionamento -= 12 * quantidade
            print(f"Veículo retirado. Valor a pagar: R${12 * quantidade:.2f}")
        elif escolha2.lower() == 'n':
            for i in range(3):
                print('.')
                time.sleep(1)
            break


if __name__ == '__main__':
    main()
