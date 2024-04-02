from time import sleep


def verificar_se_esta_dirigindo():
    return int(input('Você está dirigindo? (1 - sim | 2 - não): '))


def ler_velocidade():
    return float(input('Digite sua velocidade atual do carro: '))


def verificar_se_multa(velocidade):
    verificar = False
    if velocidade > 80:
        verificar = True
        print('Você foi multado.')
        sleep(1)
    else:
        print('Você passou tranquilamente e não foi pego pelo radar!')
    return verificar


def continuar_dirigindo():
    return int(input('Deseja continuar dirigindo? 1- sim  2- não: '))


def mostrar_multas(velocidade):
    multa = (velocidade - 80)*7
    print(f'á pagar: R${multa:.2f}')


def main():
    resposta = verificar_se_esta_dirigindo()

    while True:
        if resposta == 2:
            print('Obrigada.')
            for i in range(3):
                sleep(1)
                print('.', end='')
        if resposta == 1:
            velocidade = ler_velocidade()
            verificar = verificar_se_multa(velocidade)
            if verificar:
                mostrar_multas(velocidade)
            continuar = continuar_dirigindo()
            if continuar == 1:
                continue
            else:
                break
        break


main()