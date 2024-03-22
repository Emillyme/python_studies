import sqlite3

conn = sqlite3.connect('historico.db')
conexao = conn.cursor()
conexao.execute('''CREATE TABLE IF NOT EXISTS historico (
                    jogador1 TEXT,
                    jogador2 TEXT,
                    pontos_O INTEGER,
                    pontos_x INTEGER
                    )''')
conn.commit()
conn.close()


def inserir_dados(jogador1, jogador2, pontos_O, pontos_x):
    with sqlite3.connect('historico.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(''' INSERT INTO historico (jogador1, jogador2, pontos_O, pontos_x) VALUES (?,?,?,?)''', (jogador1, jogador2, pontos_O, pontos_x))
        conexao.commit()


def imprimir_dados():
    with sqlite3.connect('historico.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(''' SELECT * FROM historico''')
        resultado = cursor.fetchall()
        print('HISTÓRICO DE PONTOS: ')
        for linha in resultado:
            print(f"Jogador 1: {linha[0]} - Pontos: {linha[2]}")
            print(f"Jogador 2: {linha[1]} - Pontos: {linha[3]}\n")

