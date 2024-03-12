import inquirer

questions = [
    inquirer.Text('name', message="What's your name?"),
    inquirer.List('gender', message="Select your gender", choices=['Male', 'Female', 'Other']),
]

answers = inquirer.prompt(questions)

print("Hello, {}!".format(answers['name']))
print("You selected gender as: {}".format(answers['gender']))


# DIFICIL:
def controlar_tempo():
    gid = os.getpid()
    time.sleep(10)
    print('Seu tempo acabou!')
    os.kill(gid, signal.SIGTERM)


def main():
    gid = os.getpid()
    chances = 4
    vida_perdida = 0
    vida_usuario = 100

    inicio()
    numero_escondido = sortear_numero()
    tempo = threading.Thread(target=controlar_tempo)
    tempo.start()

    while True:
        chances -= 1
        vida_usuario = vida_usuario - vida_perdida

        if chances == 0 or vida_usuario <= 0:
            if vida_usuario <= 0:
                print(f'\n Você perdeu! Sua vida acabou. O número secreto era:  {numero_escondido}')
            elif chances == 0:
                print(f'\nVocê perdeu! Suas chances acabaram! \n O número era {numero_escondido}.')
            break

        chute = menu(chances, vida_usuario)

        if chute == numero_escondido:
            print(f'\nParabéns! Você acertou! O número era {numero_escondido}.')
            break
        else:
            vida_perdida = perder_vida(numero_escondido, chute)
    os.kill(gid, signal.SIGTERM)


if __name__ == '__main__':
    main()