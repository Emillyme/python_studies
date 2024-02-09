import time
def menu():
    opcao = input('''
==========================================
            AGENDA EM PYTHON
    
[1] Cadastrar contato
[2] Localizar contato
[3] Listar contatos
[4] Sair
    
Digite sua preferência: ''')

    if opcao == " " or not ('1', '2', '3', '4'):
        print(f'Valor não identificado, digite um valor valido por favor:')
        time.sleep(1.5)
        menu()

    elif opcao == "1":
        cadastrarContato()

    elif opcao == "2":
        localizarContato()

    elif opcao == '3':
        listarContato()

    elif opcao == "4":
        print('Saindo da agenda...')
        time.sleep(1)


def cadastrarContato():
    nomeContato = input('Digite o nome do contato: ')
    numContato = input('Digite o número do contato: ')
    emailContato = input('Digite o email do contato: ')

    try:
        agenda = open("agenda.txt", "a")
        dados = f'{nomeContato};{numContato};{emailContato}\n'
        agenda.write(dados)
        agenda.close()
        print('Gravado com sucesso')
    except:
        print('Erro no cadastro.')
def localizarContato():
    localizar = input('Coloque o contato que deseja localizar: ')

    for
        agenda = open("agenda.txt", "r")

def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
def main():
    menu()

main()