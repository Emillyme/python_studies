import inquirer
from sorteador_facil import main_facil
from sorteador_medio import main_medio
from sorteador_dificil import main_dificil


def main():
    print('-' * 10, '\033[1;33mBEM-VINDO ao SORTEADOR!\033[m', '-' * 10)
    questions = [
        inquirer.List('dificuldade', message="Escolha a dificuldade", choices=['Fácil', 'Médio', 'Difícil'])
    ]

    answers = inquirer.prompt(questions)

    if answers['dificuldade'] == 'Fácil':
        main_facil()
    elif answers['dificuldade'] == 'Médio':
        main_medio()
    elif answers['dificuldade'] == 'Difícil':

        main_dificil()


if __name__ == "__main__":
    main()
