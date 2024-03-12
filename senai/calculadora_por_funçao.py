import requests
from tkinter import *

def adicao(num, num2):
    y = num + num2
    print(f'A adição de {num} + {num2} é: {y}')
    return y

def main():
    num = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    while True:
        resposta = input('Você quer fazer uma adição desses dois números?')
        if resposta == 'sim':
            adicao(num, num2)
            break
        else:
            print('tanto faz.')
            break

if __name__ == '__main__':
    main()

janela = Tk()
janela.title('Calculadora')

titulo = Label(janela, text='CALCULADORA')
titulo.grid(column=0, row=0)

titulo2 = Label(janela, text='\nEscreva dois números: ')
titulo2.grid(column=0, row=1)


janela.mainloop()